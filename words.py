def print_upper_words(word_list):
    """ prints out each word in a list in capital letters and on a separate line """
    for word in word_list:
      print(word.upper())

def print_starts_with_e(word):
   """ prints each word uppercased on a separate line that begin with the letter 'e' or 'E' """
   for char in word:
      if char == 'e' or char == 'E':
         print(word.upper())

def print_uppercase_words(word_list, must_start_with):
    """ prints each word in list on a separate line and uppercased that begins with the passed in letters """
    for word in word_list:
       for letter in must_start_with:
          if word.startswith(letter):
             print(word.upper())

words = ['javascript', 'python', 'rust']
word = 'elixir'

print_upper_words(words)
print_starts_with_e(word)
print_uppercase_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
