'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
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

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        for character in self.word:
            self.word_guessed.append('_')
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []
        self.image_dic =   {0:" ____\n|   |\n|   O \n|  /|\\\n|   | \n|  / \\\n|_____",
                            1:" ____\n|   |\n|\n|\n|\n|  \n|_____",
                            2:" ____\n|\n|\n|\n|\n|  \n|_____",
                            3:"\n|\n|\n|\n|\n|  \n|_____",
                            4:"\n_____"}

        print(f"The mystery word has {len(self.word)} characters.\n")
        print(f'{self.word_guessed}, \n')


    def check_letter(self, letter) -> None:
        
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''

        if letter in self.word:
            for i, character in enumerate(self.word):
                if character == letter:
                    self.word_guessed[i] = letter
            self.num_letters = self.num_letters - 1
            print(f'Nice! {letter} is in the word\n')
            
        else:
            self.num_lives = self.num_lives - 1 
            print(f'Sorry, {letter} is not in the word.\n')
            print(self.image_dic[self.num_lives])
            print(f'You have {self.num_lives} lives left.\n')
            

    def ask_letter(self):
        
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''

        valid_letter = False
        while valid_letter == False:
            guess = input('Input your guess letter: ')
            print('\n')
            letter = guess.lower()
            if len(letter) > 1:
                print('Please, enter just one character\n')
            elif len(letter) == 0:
                print('Please, enter at least one character\n')
            elif letter in self.list_letters:
                    print(f"{letter} was already tried\n")
            else:
                valid_letter = True
                self.list_letters.append(letter)
                self.check_letter(letter)

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    finished = False
    while finished == False:
        game.ask_letter()
        if game.num_lives == 0:
            print(f"You ran out of lives. The word was {game.word}")
            finished = True
            break
        
        elif game.num_letters ==0:
            print(game.word_guessed, '\n')
            print('Congratulations, you won!')
            finished = True
            break
        print(game.word_guessed, '\n')
        
        


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
