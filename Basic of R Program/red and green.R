# Install ggplot2 package if not already installed
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}

# Load the ggplot2 library
library(ggplot2)

# Function to draw a heart shape
draw_heart <- function(color) {
  heart <- data.frame(
    x = c(-1, 0, 1, -2, -1, 0, 1, 2, -1.5, -0.5, 0.5, 1.5),
    y = c(2, 2, 2, 1, 1, 1, 1, 2, 2.5, 2.5, 2.5, 2.5)
  )
  
  ggplot(heart, aes(x = x, y = y)) +
    geom_polygon(fill = color) +
    coord_fixed() +
    theme_void()
}

# Create a plot with a red heart
red_heart <- draw_heart("red")
print(red_heart)

