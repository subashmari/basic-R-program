print("Finite Probability: Tossing a Coin 'n' times")

sample.space <- c('H', 'T')  # You missed a closing single quote in 'T'

count <- as.integer(readline(prompt = "Enter how many times to toss the coin: "))

outcome <- sample(sample.space, count, replace = TRUE)

print("Outcomes:")
print(outcome)

df_outcome <- data.frame(table(outcome))

df_prob <- cbind(df_outcome, Probability = prop.table(df_outcome$Freq))

print("Tossing Result:")
print(df_prob)

cat("No. of outcomes =", count)