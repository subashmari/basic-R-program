# Load the required packages
if (!requireNamespace("corrplot", quietly = TRUE)) {
  install.packages("corrplot")
}
if (!requireNamespace("RColorBrewer", quietly = TRUE)) {
  install.packages("RColorBrewer")
}
library(corrplot)
library(RColorBrewer)

# Load the mtcars dataset
data(mtcars)

# Calculate correlations
M <- cor(mtcars[, c(1, 3, 4, 5, 6, 7)])
cat("Columns taken for analysis:")
cat(colnames(M))

cat("Karl Pearson's Correlation Coefficients:")
cat(round(M, 2))

# Pair Plot
pairs(mtcars[, c(1, 3, 4, 5, 6, 7)], panel = panel.smooth, main = "Pairs Plot")

# Correlation Plot
corrplot(M, title = 'Correlation Plot', method = 'ellipse')