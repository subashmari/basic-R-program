is_palindrome <- function(input_string) {
  # Remove spaces and convert to lowercase
  cleaned_string <- gsub("\\s+", "", tolower(input_string))

  # Check if the cleaned string is equal to its reverse
  return(cleaned_string == rev(strsplit(cleaned_string, '')[[1]]))
}

# Test the function
input <- "A man a plan a canal Panama"
result <- is_palindrome(input)

if (result) {
  cat("The input string is a palindrome.\n")
} else {
  cat("The input string is not a palindrome.\n")
}
