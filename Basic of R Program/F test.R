group1 <- rnorm(100, mean = 0, sd = 1)
group2 <- rnorm(100, mean = 1, sd = 1)
t_test_result <- t.test(group1, group2)
boxplot(group1, group2, names = c("Group 1", "Group 2"), col = c("blue", "red"), main = "Box Plot")
print(t_test_result)
factor1 <- rep(c("A", "B"), each = 50)
factor2 <- rep(c("X", "Y"), each = 50)  # Ensure both factors have the same length
data <- rnorm(100, mean = 0, sd = 1)
anova_result <- aov(data ~ factor1 * factor2)
interaction.plot(factor1, factor2, data, type = "b", col = c("blue", "red"), pch = c(1, 19))
print(summary(anova_result))

