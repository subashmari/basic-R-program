# Load the dplyr package (if not already loaded)
library(dplyr)

# Create a sample dataset
data <- c(1, 2, 2, 3, 4, 4, 5, 6, 7)

# Use the n_distinct() function to count distinct elements
distinct_count <- n_distinct(data)

# Print the count
print(distinct_count)
