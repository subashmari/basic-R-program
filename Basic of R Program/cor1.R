# Load the required packages
if (!requireNamespace("corrplot", quietly = TRUE)) {
  install.packages("corrplot")
}
if (! requireNamespace("RColorBrewer", quietly = TRUE)) {
  install.packages("RColorBrewer")
}
library(corrplot)
library(RColorBrewer)

# Load the mtcars dataset
data(mtcars)

# Calculate correlations
M <- cor(mtcars[, c(1, 3, 4, 5, 6, 7])
                cat("Columns taken for analysis:")
                cat(colnames(M))
                
                cat("Karl Pearson's Correlation Coefficients:")
                cat(round(M, 2))
                
                # Pair Plot
                pairs(mtcars[, c(1, 3, 4, 5, 6, 7)], panel = panel.smooth, main = "Pairs Plot")
                
                # Correlation Plot
                corrplot(M, title = 'Correlation Plot', method = 'ellipse')
                
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
                