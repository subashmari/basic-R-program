# Load the ggplot2 package
library(ggplot2)

# Function to plot a heart shape
plot_heart <- function() {
  t <- seq(0, 2 * pi, length.out = 100)
  x <- 16 * sin(t)^3
  y <- 13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t)
  
  heart_data <- data.frame(x = x, y = y)
  
  # Create the heart shape plot
  ggplot(heart_data, aes(x, y)) +
    geom_polygon(fill = "red", color = "black") +
    coord_fixed() +
    theme_void()
}

# Call the function to plot the heart shape
plot_heart()
