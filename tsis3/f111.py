def is_palindrome(word):
    """
    Checks whether a word or phrase is a palindrome.

    Args:
        word (str): The input word or phrase.

    Returns:
        bool: True if the word/phrase is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    cleaned_word = "".join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]

# Example usage
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
