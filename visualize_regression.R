library(ggplot2)

# Load the data
data <- read.csv('data/segmented_customer_data.csv')

# Create a regression plot for the entire dataset
plot <- ggplot(data, aes(x=age, y=annual_income, color=factor(cluster))) +
  geom_point() +
  geom_smooth(method='lm', se=FALSE) +
  labs(title="Regression Analysis", x="Age", y="Annual Income", color="Cluster") +
  theme_minimal()

# Save the plot
ggsave("static/cluster_regression_plot.png", plot)
