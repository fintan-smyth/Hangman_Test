# Hangman_Test

For this project we were tasked to program a simple hangman game using python. I used simple python tools such as loops, if statements and object oriented programming concepts to request an input, check if it was valid, check the letter against the word, and give an appropriate output, exiting the program when the game was complete.

---

# Milestone 1


For milestone 1 we were required to program the first component of the `ask_letter` method, which prompts the user to input a letter and proceed if the input is determined to be valid. A valid input in this case is defined as one that constitutes a single character. If the input is not valid it will output an appropriate error message and continue to prompt the user until a valid input is given. Once a valid input is received the `ask_letter` method will finish and the code will proceed.

To achieve this I used the following code:
``` python
def ask_letter(self)
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

When the `ask_letter` method is called the game will now prompt the user and display the correct message when inputs are given.

![Milestone 1 output](images/Milestone%201%20ouptut.jpg)

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
- For the `word_guessed` attribute I created an empty list and assigned it to the attribute. Then, I used a `for` loop to iterate over the characters of the randomly chosen word, and for each character an underscore is appended to the list, resulting in a list containing an underscore for each letter of the word.
- To determine the number of unique characters in the word, I first passed the the chosen word into the `set` function to construct a set consisting of the unique characters from the word. This set is then passed into the `len` function to find the number of unique characters in the word, and this is assigned to the `num_letters` attribute. 
- The `num_lives` attribute is simply assigned to be equal to the `num_lives` parameter.
- For the `list_letters` attribute an empty list is created, as initially no letters have been tried, to be populated later when attempts are made.
- The two required statements are then printed, using f-strings to format them to contain the length of the `word` attribute, and the `word_guessed` list respectively.

Additionally, milestone 2 required us to add to the `ask_letter` method such that it would now also check if the input letter had already been tried, and only proceed if this was not the case. To do so I made the following changes to the contents of the loop contained in the `ask_letter` method:
``` python
    elif letter in self.list_letters:
       print(f"{letter} was already tried\n")
    else:
        valid_letter = True
        self.list_letters.append(letter)
```
- An additional `elif` statement was added to the loop which checks if the letter is in the `list_letters` list. If so, the output `{letter} was already tried` is given and the loop restarts.
- If not, the loop proceeds to the `else` statement, which now also appends the guessed letter to the `list_letters` list.

Now when the game is initialised the two required messages are printed. The game will now also reject a letter that has already been tried and prompt for a different input.

![Milestone 2](images/Milestone%202.jpg)

---
# Milestone 3

For the third milestone, we were required to complete the `check_letter` method, which is used to check if the letter is contained in the word. If it is a congratulations message is displayed, the `word_guessed` list is updated to include the new letter and displayed, and the `num_letters` attribute is reduced by one. If the letter is not included an error message is displayed and the `num_lives` attribute is reduced by one.

To achieve this I used the following code:
```python
    def check_letter(self, letter):
        if letter in self.word:
            for i, character in enumerate(self.word):
                if character == letter:
                    self.word_guessed[i] = letter
            self.num_letters = self.num_letters - 1
            print(f'Nice! {letter} is in the word\n')
            print(self.word_guessed, '\n')
            
        else:
            self.num_lives = self.num_lives - 1 
            print(f'Sorry, {letter} is not in the word.\n')
            if self.num_lives == 1:
                print(f'You have {self.num_lives} life left.\n')
            else:
                print(f'You have {self.num_lives} lives left.\n')
```
- An `if` statement is used to check if the letter is contained in the word.
- If it is: 
    - The `enumerate` function is used to generate an enumerate object consisting of each letter in order and its index, which is then iterated over.
    - If the character from the word is equal to the letter that was guessed, the item(s) in the `word_guessed` list with the index of the characters matching the letter guess are replaced with said letter.
    - The `num_letters` attribute is then reduced by one.
    - An f-string is used to print the output `Nice! {letter} is in the word`
    - The updated `word_guessed` list is then printed.
- If the letter is not in the word:
    - The `num_lives` attribute is reduced by one.
    - An f-string is used to print `Sorry, {letter} is not in the word.` followed by `You have {self.num_lives} life left.` if the number of remaining lives is equal to one. Otherwise, `You have {self.num_lives} lives left.` is displayed.

Finally, the `ask_letter` method must be updated to call the `check_letter` method on the letter once a valid input is received. To do this the final `else` clause is changed to include `self.check_letter(letter)`:
``` python
    else:
        valid_letter = True
        self.list_letters.append(letter)
        self.check_letter(letter)
```

Now, when an incorrect letter is guessed the game will inform the player and remove a life. When a correct letter is guessed, the player is informed and the `word_guessed` list is displayed, with every instance of the letter correctly replaced.

![Milestone 3](images/Milestone%203.jpg)

---

# Milestone 4

For the final milestone, the logic of the game needs to be coded. The game must iteratively prompt the player for an input until either all the letters have been guessed or the player runs out of lives. In either case, an appropriate message should be displayed before exiting the game completely. My code to achieve this is as follows:
```python
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    finished = False
    while finished == False:
        game.ask_letter()
        if game.num_lives == 0:
            print(f"You ran out of lives. The word was {game.word}")
            finished = True
        elif game.num_letters == 0:
            print('Congratulations, you won!')
            finished = True
```

- Firstly an instance of the `Hangman` class is called with parameters `word_list` and `num_lives = 5`.
- The variable `finished` corresponding to whether the game has finished yet is initialised as `False`.
- A `while` loop is created to execute repeatedly as long as `finished` is equal to `False`.
- Within the loop the `ask_letter` method is then called.
- Once the `ask_letter` method has run an `if`/`elif` pair of statements is used to determine if the game is complete.
    - If `num_lives` is equal to zero, the statement `You ran out of lives. The word was {game.word}` is displayed and the `finished` variable is set to `True` causing the loop to no longer repeat.
    - Otherwise, if `num_letters` is equal to zero, the statement `Congratulations, you won!` is displayed and the `finished` variable is set to `True` causing the loop to no longer repeat.
    - If neither are the case, the `finished` variable remains `False` and the loop continues.

Finally, to play the game when the program is run the following code is included:
```python
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
```
- If the `__name__` variable is equal to `__main__`, meaning that the code is running as the main program and not being imported, then the contents of the if clause are run:
    - A `word_list` variable is created containing a list of words to be selected from.
    - The `play_game` method is then called on this list of words.

The game will now continue to prompt for guesses until either of the game finishing conditions are met, upon which the appropriate closing message is displayed and the program finishes.

![](images/Milestone%204%20a.jpg)![](images/Milestone%204%20b.jpg)

---

# Bonus Milestone

For the bonus milestone it was necessary to devise a method to display a visual representation of the player's remaining lives, progressively revealing more of the hangman image as lives are lost. To achieve this I did the following:
```python
self.image_dic =   {0:" ____\n|   |\n|   Q\n|  /|\\\n|   | \n|  / \\\n|_____",
                    1:" ____\n|   |\n|   0\n|\n|\n|  \n|_____",
                    2:" ____\n|\n|\n|\n|\n|  \n|_____",
                    3:"\n|\n|\n|\n|\n|  \n|_____",
                    4:"\n_____"}
```
- I first added the attribute `image_dic` to the `__init__` method and assigned to it a dictionary containing:
    - __Keys__ corresponding to the number of possible lives remaining once at least one incorrect guess has been made (4 - 0) 
    - __Values__ consisting of the ASCII image to be displayed at the appropriate number of lives remaining  
```python
        else:
            self.num_lives = self.num_lives - 1 
            print(f'Sorry, {letter} is not in the word.\n')
            print(self.image_dic[self.num_lives],'\n')
            print(f'You have {self.num_lives} lives left.\n')
```
- The final `else` clause of the `check_letter` method, executed when an incorrect letter is input, is then updated to print the value from `image_dic` with a key equal to the number of lives remaining `num_lives`.

The game now shows progressively more of the hangman image as the player makes incorrect guesses and loses lives.

![](images/bonus%20milestone%201.jpg) ![](images/bonus%20milestone%202.jpg)

---

# Conclusion

In conclusion thsi project gave me good experience in bringing together the various python concepts I have learned. I had some experience with python prior to starting the AICore course, but largely with running select lines of code for example in jupyter notebook. This project helped me gain an understanding of how a python program in its entirety is created and provided good practice with using python to solve the various problems necessary to complete the project.

To improve on the program I have created, I could find a way to automatically display a correct proportion of the hangman image should a different number of lives be selected as a game parameter. It would currently only work with the default selection of five lives, as there is a specific image corresponding to each of the remaining lives.