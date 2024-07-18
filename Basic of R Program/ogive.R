height_data <- c(170, 165, 175, 162, 180, 168, 172, 178, 185, 169)
x_values <- sort(unique(height_data))
cum_freq_less_than <- 1 - ecdf(height_data)(x_values)
cum_freq_more_than <- ecdf(height_data)(x_values)
plot(x_values, cum_freq_less_than, type = "b", pch = 19, col = "red",
     xlab = "Height", ylab = "Cumulative Frequency", main = "Ogives")
lines(x_values, cum_freq_more_than, type = "b", pch = 19, col = "blue")
legend("topright", legend = c("Less Than Ogive", "More Than Ogive"),
       col = c("red", "blue"), pch = 19)
