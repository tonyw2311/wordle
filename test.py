
import sys

def is_word_forbidden_to_use(word, forbidden_list):
    for char in forbidden_list:
        if char != '#' and (char in word):
            return True
    return False

def is_word_using_all_near_guesses(word, near_guess_list):
    for character in near_guess_list:
        if character != '#' and character not in word:
            return False
    return True

def is_word_using_exact_guesses(word, guess_list):
    for index, char in enumerate(guess_list):
        if char != '#' and char != word[index]:
            return False
    return True

# first argument is the correct guess made so far: ie. ###g#
# second argument are the characters that are forbidden: ie. staer
# third argument is the near-match from guesses made so far: res

guess_list = list(sys.argv[1])
forbidden_list = list(sys.argv[2])
near_guess_list = list(sys.argv[3])

print(f'guess: {guess_list}')
print(f'forbidden_list: {forbidden_list}')
print(f'near guess: {near_guess_list}')


word_suggestions = []
with open('words.txt','r') as reader:
    for word in reader:
        if is_word_forbidden_to_use(word, forbidden_list):
           continue 

        if not is_word_using_all_near_guesses(word,near_guess_list):
            continue
        
        if not is_word_using_exact_guesses(word, guess_list):
            continue
        word_suggestions.append(word)
        if len(word_suggestions) == 10:
            break

        
print(f'Wordle suggestions: {word_suggestions}')
