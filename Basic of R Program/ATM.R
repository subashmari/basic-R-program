# Function to simulate ATM functionality
atm_simulation <- function() {
  account_balance <- 1000  # Starting account balance
  
  print("Welcome to the ATM!")
  
  while (TRUE) {
    print("\nSelect an option:")
    print("1. Check Account Balance")
    print("2. Withdraw Money")
    print("3. Exit")
    
    choice <- as.numeric(readline("Enter your choice (1/2/3): "))
    
    if (is.na(choice) || choice < 1 || choice > 3) {
      print("Invalid choice. Please try again.")
      next
    }
    
    if (choice == 1) {
      print(paste("Your account balance is $", account_balance))
    } else if (choice == 2) {
      amount <- as.numeric(readline("Enter the amount to withdraw: "))
      
      if (is.na(amount) || amount <= 0) {
        print("Invalid amount. Please enter a valid amount.")
        next
      }
      
      if (amount > account_balance) {
        print("Insufficient funds.")
        next
      }
      
      account_balance <- account_balance - amount
      print(paste("You have withdrawn $", amount, ". Your remaining balance is $", account_balance))
    } else if (choice == 3) {
      print("Thank you for using the ATM. Have a great day!")
      break
    }
  }
}

# Run the ATM simulation
atm_simulation()

