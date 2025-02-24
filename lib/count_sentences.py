#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value  # Use the setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ''  # Set to empty string if the value is not a string
        else:
            self._value = new_value

    def is_sentence(self):
        """Returns True if the value ends with a period, False otherwise."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the value ends with a question mark, False otherwise."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark, False otherwise."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Counts the number of sentences in the value."""
        # Replace multiple punctuation marks with a single one
        cleaned_value = self.value.replace('!', '.').replace('?', '.')
        # Split the string by the period and filter out empty strings
        sentences = [sentence.strip() for sentence in cleaned_value.split('.') if sentence.strip()]
        return len(sentences)

# test
if __name__ == "__main__":
    my_string = MyString("This is a string! It has three sentences. Right?")
    print(my_string.count_sentences())  # Output: 3
    print(my_string.is_sentence())       # Output: False
    print(my_string.is_question())       # Output: False
    print(my_string.is_exclamation())    # Output: True