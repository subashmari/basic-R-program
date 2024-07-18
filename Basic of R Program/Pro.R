# Dataset: mtcars

# Dataset: mtcars

#install.packages('complot')

#install.packages('RColorBrewer')

#library(complot)

#library(RColorBrewer)

# Install and load the required packages
if (!requireNamespace("complot", quietly = TRUE)) {
  install.packages("complot")
}
if (!requireNamespace("RColorBrewer", quietly = TRUE)) {
  install.packages("RColorBrewer")
}
library(complot)
library(RColorBrewer)

cat('Features in the dataset')
cat(colnames(mtcars))

# Calculate correlations
M <- cor(mtcars[, c(1, 3, 4, 5, 6, 7)])
cat("Columns taken for analysis:")
cat(colnames(M))

cat("Karl Pearson's Correlation Coefficients:")
cat(round(M, 2))

# Pair Plot
pairs(mtcars[, c(1, 3, 4, 5, 6, 7)], panel = panel.smooth, main = "Pairs Plot")

# Correlation Plot
complot(M, title = 'Correlation Plot', type = "upper", method = 'square')
complot(M, title = 'Correlation Plot', type = 'lower', method = 'ellipse')
corrplot(M, title = 'Correlation Plot', type = "lower", method = 'number')
complot.mixed(M, title = 'Correlation Plot', lower = 'circle', upper = 'pie')
complot(M, title = 'Correlation Plot', type = 'lower', order = 'hclust')
corrplot(M, title = 'Correlation Plot', type = 'lower', order = 'FPC')
complot(M, title = 'Correlation Plot', type = 'full', order = 'hclust', addrect = 2)


cat("SIMPLE LINEAR REGRESSION")
simple_LR <- lm(mpg ~ hp, data = mtcars)
intercept1 <- round(as.numeric(simple_LR$coefficients[1]), 2)
slope1 <- round(as.numeric(simple_LR$coefficients[2]), 2)
simple_LR_eq <- paste("mpg =", intercept1, "+", slope1, "* hp")
cat("Generated Model is: ")
cat(simple_LR_eq)
cat("Summary of the Model:")
print(summary(simple_LR))

plot(mtcars$hp, mtcars$mpg, col = "blue", main = "hp & mpg Regression")
abline(simple_LR, col = "red", lwd = 2)
xlabel <- "Horse Power"
ylabel <- "Miles Per Gallon"
title(main = "hp & mpg Regression", xlab = xlabel, ylab = ylabel)

cat("MULTIPLE LINEAR REGRESSION")
multiple_LR <- lm(mpg ~ hp + disp + wt, data = mtcars)
intercept2 <- round(as.numeric(multiple_LR$coefficients[1]), 2)
slope_hp <- round(as.numeric(multiple_LR$coefficients[2]), 2)
slope_disp <- round(as.numeric(multiple_LR$coefficients[3]), 2)
slope_wt <- round(as.numeric(multiple_LR$coefficients[4]), 2)
multiple_LR_eq <- paste("mpg =", intercept2, "+", slope_hp, "* hp", "+", slope_disp, "* disp", "+", slope_wt, "* wt")
cat("Generated Model is: ")
cat(multiple_LR_eq)
cat("Summary of the Model:")
print(summary(multiple_LR))
