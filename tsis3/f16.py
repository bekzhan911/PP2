def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words to form the final sentence
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

# Example usage
user_input = input("Enter a sentence: ")
reversed_result = reverse_sentence(user_input)
print(reversed_result)
