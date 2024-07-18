factor1 <- rep(c("A", "B"), each = 50)
factor2 <- rep(c("X", "Y"), each = 50)  # Ensure both factors have the same length
data <- rnorm(100, mean = 0, sd = 1)
anova_result <- aov(data ~ factor1 * factor2)
interaction.plot(factor1, factor2, data, type = "b", col = c("blue", "red"), pch = c(1, 19))
print(summary(anova_result))
