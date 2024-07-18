values <- c(5, 2, 8, 2, 4, 8, 1, 6, 3,7,8,10,253,123,756)

mean_value <- mean(values)

median_value <- median(values)

mode_value <- as.numeric(names(table(values))[table(values) == max(table(values))])

print(paste("Mean:", mean_value))

print(paste("Median:", median_value))

print(paste("Mode:", mode_value))

print(paste("thank you"))
