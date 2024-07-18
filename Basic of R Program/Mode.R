data <- c(5, 2, 8, 2, 4, 8, 1, 6, 3)
mode_value <- unique(my_vector)[which.max(tabulate(match(data, unique(data))))]
print(paste("Mode:", mode_value))
