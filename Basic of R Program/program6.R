# Binomial Distribution
x <- seq(1, 100, by = 2)
y <- dbinom(x, 50, 0.5)
print('Binomial Distribution')
print(y)
plot(x, y, main = 'Binomial Distribution')
lower <- as.integer(readline(prompt = 'Lower: '))
upper <- as.integer(readline(prompt = 'Upper: '))
bdist <- sum(dbinom(lower:upper, 100, 0.5))
print(paste('Binomial Distribution: P(', lower, '< x <', upper, ') = ', bdist))

# Normal Distribution
print('Normal Distribution')
start <- as.integer(readline(prompt = 'Start value: '))
end <- as.integer(readline(prompt = 'End value: '))
step <- as.numeric(readline(prompt = 'Step Value: '))
x <- seq(start, end, step)
m <- as.numeric(readline(prompt = 'Enter mean for the distribution: '))
s <- as.numeric(readline(prompt = 'Enter standard Deviation for the distribution: '))
y <- dnorm(x, mean = m, sd = s)
print('Normal Distribution')
print(y)
plot(x, y, main = 'Normal Distribution')
20
