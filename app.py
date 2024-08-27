from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import plotly.express as px
import plotly.io as pio
import os

app = Flask(__name__)

# Load default model and data
kmeans = joblib.load(os.path.join('models', 'kmeans_model.pkl'))
data = pd.read_csv(os.path.join('data', 'segmented_customer_data.csv'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    customer_id = int(request.json['customer_id'])
    customer = data[data['customer_id'] == customer_id]
    
    if customer.empty:
        return jsonify({"error": "Customer not found."}), 404
    
    cluster = customer['cluster'].values[0]
    recommendations = {
        0: ["Product A", "Product B"],
        1: ["Product C", "Product D"],
        2: ["Product E", "Product F"],
        3: ["Product G", "Product H"],
        4: ["Product I", "Product J"]
    }
    
    # Regression Plot (age vs. annual_income)
    fig = px.scatter(data, x='age', y='annual_income', color='cluster', trendline='ols')
    fig.update_layout(title='Regression Analysis')
    graph_html = pio.to_html(fig, full_html=False)
    
    # Convert non-JSON serializable types
    return jsonify({
        "customer_id": int(customer_id),
        "cluster": int(cluster),  # Ensure cluster is an int
        "recommendations": recommendations.get(cluster, ["No recommendations"]),
        "graph": graph_html
    })

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and file.filename.endswith('.csv'):
        filename = os.path.join('data', 'uploaded_customer_data.csv')
        file.save(filename)
        
        try:
            # Re-run preprocessing and segmentation
            os.system('python preprocess_data.py')  # Consider calling these directly in Python
            os.system('python customer_segmentation.py')
        except Exception as e:
            return jsonify({"error": f"Failed to process the file: {str(e)}"}), 500
        
        return jsonify({"message": "File uploaded and processed successfully."})
    
    return jsonify({"error": "Invalid file type."}), 400

if __name__ == '__main__':
    app.run(debug=True)
