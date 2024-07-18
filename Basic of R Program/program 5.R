# Multiplication Law of Probability
# P(A and B) = P(A) * P(B|A)
# Deck of Cards
# Assumption: Event A as Suit, Event B as Suit, without replacement
# Define the suits and faces of the cards
suits <- c('Diamond', 'Club', 'Heart', 'Spade')
faces <- c('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
deck <- expand.grid(Suit = suits, Face = faces)
total.cards <- nrow(deck)
event.A <- readline(prompt = "Enter the first suit: ")
prob.A <- nrow(deck[deck$Suit == event.A, ])/total.cards
cat("Prob. of first suit =", prob.A, "\n")
event.B <- readline(prompt = "Enter the second suit: ")
prob.B <- nrow(deck[deck$Suit == event.B, ])/total.cards
cat("Prob. of second suit =", prob.B, "\n")
prob.A.and.B <- prob.A * prob.B
cat("Prob. of first suit =", event.A, "and second suit =", event.B, "is", prob.A.and.B, "\n")
