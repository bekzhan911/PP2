def snake_to_camel(text):
    return ''.join(word.title() for word in text.split('_'))

# Example usage
snake_string = "geeksforgeeks_is_best_for_geeks"
print("Original string:", snake_string)
print("Camel case string:", snake_to_camel(snake_string))
