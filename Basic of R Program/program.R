# Function to check if a string is a palindrome
is_palindrome <- function(input_string) {
  # Remove spaces and convert to lowercase
  cleaned_string <- gsub("\\s+", "", tolower(input_string))
  
  # Reverse the cleaned string
  reversed_string <- rev(strsplit(cleaned_string, NULL)[[1]])
  
  # Compare the cleaned string with the reversed string
  is_palindrome <- all(cleaned_string == reversed_string)
  
  return(is_palindrome)
}

# Test the function
word_or_phrase <- "Able was I ere I saw Elba"
if (is_palindrome(word_or_phrase)) {
  cat(sprintf('"%s" is a palindrome.', word_or_phrase))
} else {
  cat(sprintf('"%s" is NOT a palindrome.', word_or_phrase))
}

