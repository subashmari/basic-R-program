# Install ggplot2 package if not already installed
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}

# Load the ggplot2 library
library(ggplot2)

# Create some example data for the scatter plot
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 1, 6, 3)

# Create a scatter plot using ggplot2
scatter_plot <- ggplot(data.frame(x, y), aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Scatter Plot Example", x = "X-axis", y = "Y-axis")

# Display the plot
print(scatter_plot)
