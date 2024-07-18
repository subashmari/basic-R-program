print("Infinite Probability: Tossing a Coin till Head")

sample_space <- c("H", "T") 

count <- 0

while (TRUE) {
  outcome <- sample(sample_space, 1)
  count <- count + 1
  
  if (outcome == "H") {
    print(outcome)
    break
  }
  
  print(outcome)
}

cat("No. of trials:", count)
