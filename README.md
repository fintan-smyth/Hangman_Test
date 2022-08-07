# Hangman_Test

For this project we were tasked to program a simple hangman game using python. I used simple python tools such as loops, if statements and object oriented programming concepts to request an input, check if it was valid, check the letter against the word, and give an appropriate output, exiting the program when the game was complete.

---

# Milestone 1


For milestone 1 we were required to program the first component of the `ask_letter` method, which prompts the user to input a letter and proceed if the input is determined to be valid. A valid input in this case is defined as one that constitutes a single character. If the input is not valid it will output an appropriate error message and continue to prompt the user until a valid input is given. Once a valid input is received the `ask_letter()` method will finish and the code will proceed.

To achieve this I used the following code:
``` python
define ask_letter(self)
    valid_letter = False    
    while valid_letter == False:
        letter = input('Input your guess letter: ').lower()
        print('\n')
        if len(letter) > 1:
            print('Please, enter just one character\n')
        elif len(letter) == 0:
            print('Please, enter at least one character\n')
        else:
            valid_letter = True
```
- I first created a variable representing whether a valid input had been received, before creating a `while` loop that would continue to execute as long as this variable remained false.

- Within the body of the loop the user is asked for an input using the `input` function, and this input is then made lowercase (for easier processing later) and assigned to a variable `letter`.

- A series of `if`, `elif`, and `else` statements are then used to determine if the input is valid using the `len` function. 

     - If the length of the input string is greater than one, the output `Please, enter just one character` is given and the loop restarts.

    - Otherwise, if the length of the string equal to zero, the output `Please, enter at least one character` is given and the loop restarts.

    - Finally, if the length of the input string is neither greater than one nor zero, therefore being equal to 1 as it is a positive integer, the `valid_letter` variable is changed to `True`, causing the loop to exit.
- Additionally, newlines `\n` were added between ouptuts to aid in readability.

---

# Milestone 2

For the second milestone it was necessary to define the `__init__` method, setting up with a series of attributes provided in the docstring. 
```
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
```

Upon initialisation the method should also print two messages: A statement informing the user of the length of the word, and the `word_guessed` list.

Here is the code I used to achieve this:
``` python
def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        for character in self.word:
            self.word_guessed.append('_')
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []
        print(f"The mystery word has {len(self.word)} characters.\n")
        print(f'{self.word_guessed}, \n')
```
- I used the `random.choice` method from the `random` module to select a random word from `word_list` and assign it to the `word` attribute.
- For the `word_guessed` attribute I created an empty list and assigned it to the attribute. Then, I used a `for` loop to iterate over the characters of the randomly chosen word, and for each character an underscore is appended to the list, thus resulting in a list containing an underscore for each letter of the word.
- To determine the number of unique characters in the word, I first passed the the chosen word into the `set` function to construct a set consisting of the unique characters from the word. This set is then passed into the `len` function to find the number of unique characters in the word, and this is assigned to the `num_letters` attribute. 
- The `num_lives` attribute is simply assigned the `num_lives` parameter.
- For the `list_letters` attribute an empty list is created, as initially no letters have been tried, to be populated later when attempts are made.
- The two required statements are then printed, using f-strings to format them to contain the length of the `word` attribute, and the `word_guessed` list respectively.

Additionally, milestone 2 required us to add to the `ask_letter` method such that it would now also check if the input letter had already been tried, and only proceed if this was not the case. To do so I made the following addition to the contents of the loop contained in the `ask_letter` method:
``` python
    elif letter in self.list_letters:
       print(f"{letter} was already tried\n")
    else:
        valid_letter = True
        self.list_letters.append(letter)
```
- An additional `elif` statement was added to the loop which checks if the letter is in the `list_letters` list. If so, the output `{letter} was already tried` is given and the loop restarts.
- If not, the loop proceeds to the `else` statement, which now also appends the guessed letter to the `list_letters` list.
---
# Milestone 3

