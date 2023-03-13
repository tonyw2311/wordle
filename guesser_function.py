import re

def is_word_forbidden_to_use(word, forbidden_list):
    for char in forbidden_list:
        if (char in word):
            return True
    return False

def is_word_using_all_near_guesses(word, near_guess_list, near_dict):
    for index, char in enumerate(near_guess_list):
        if (char not in word) or ((char in word) and (str(word.index(char)) in near_dict[char])):
            return False
    return True

def is_word_using_exact_guesses(word, guess_list):
    for index, char in enumerate(guess_list):
        if char != '#' and char != word[index]:
            return False
    return True

def guesser(word,forbidden_list,near_guess_list,exact_list,near_dict):

    #Iterates through the list given from webscraping and assigns them to appropriate values
    for index, letter_guessed  in enumerate(word):
        letter_found = letter_guessed[0]
        value_of_letter = letter_guessed[2:]
        if value_of_letter == 'absent':
            forbidden_list.append(letter_found)
        if value_of_letter == 'present':
            near_guess_list.append(letter_found)
            if letter_found in near_dict:
                near_dict[letter_found] += str(index)
            else:
                near_dict[letter_found] = str(index)
        if value_of_letter == 'correct':
            exact_list[index] = letter_found

    with open('words.txt','r') as reader:
        for word in reader:
            if is_word_forbidden_to_use(word, forbidden_list):
                continue 
            
            if not is_word_using_all_near_guesses(word,near_guess_list, near_dict):
                continue
            
            if not is_word_using_exact_guesses(word, exact_list):
                continue

            return word, forbidden_list, near_guess_list, exact_list, near_dict


#previous guesser function with shadowroot
""" def guesser(word_guessed,forbidden_list,near_guess_list,exact_list,near_dict):

    #Iterates through the list given from webscraping and assigns them to appropriate values
    for index, letter in enumerate(word_guessed):
        letter_found = re.search('letter="(.*)" evaluation',letter).group(1)
        value_of_letter = re.search('evaluation="(.*)" reveal',letter).group(1)

        if value_of_letter == 'absent':
            forbidden_list.append(letter_found)

        if value_of_letter == 'present':
            near_guess_list.append(letter_found)
            if letter_found in near_dict:
                near_dict[letter_found] += str(index)
            else:
                near_dict[letter_found] = str(index)

        if value_of_letter == 'correct':
            exact_list[index] = letter_found


    with open('words.txt','r') as reader:
        for word in reader:
            if is_word_forbidden_to_use(word, forbidden_list):
                continue 
            
            if not is_word_using_all_near_guesses(word,near_guess_list, near_dict):
                continue
            
            if not is_word_using_exact_guesses(word, exact_list):
                continue

            return word, forbidden_list, near_guess_list, exact_list, near_dict """
            



# first argument is the correct guess made so far: ie. ###g#
# second argument are the characters that are forbidden: ie. staer
# third argument is the near-match from guesses made so far: res


""" guess_list = list(sys.argv[1])
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
 """