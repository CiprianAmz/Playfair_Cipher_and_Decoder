"""Author: Amzuloiu Andrei-Ciprian"""

import string
import regex as re

"""Used to compute the polybius square"""
def get_polybius_square(key):
    used_i_or_j = False
    
    # the list of letters from key
    key_letter_list = list(key.upper())

    # remove duplicates
    key_letter_list = list(dict.fromkeys(key_letter_list))
    
    #the list of letters from the alphabet
    alphabet_list = list(string.ascii_uppercase)
    
    # the polybius square is saved in result_list
    result_list = [list(range(5)), list(range(5)), list(range(5)), list(range(5)), list(range(5))]

    # compute the poybius square
    for i in range(5):
        for j in range(5):
            if key_letter_list:
                result_list[i][j] = key_letter_list.pop(0)

                if used_i_or_j is False:
                    if result_list[i][j] == 'I' or result_list[i][j] == 'J':
                        result_list[i][j] = 'I'
                        used_i_or_j = True
                else:
                    if result_list[i][j] == 'I' or result_list[i][j] == 'J':
                        result_list[i][j] = key_letter_list.pop(0)
                
                alphabet_list.pop(alphabet_list.index(result_list[i][j]))                
            else:
                result_list[i][j] = alphabet_list.pop(0)

                if used_i_or_j is False:
                    if result_list[i][j] == 'I' or result_list[i][j] == 'J':
                        result_list[i][j] = 'I'
                        used_i_or_j = True
                else:
                    if result_list[i][j] == 'I' or result_list[i][j] == 'J':
                        result_list[i][j] = result_list[i][j] = alphabet_list.pop(0)

    return result_list

"""Get the pair positions from polybius square"""
def get_positions(square, pair):
    position = [[-1, -1], [-1, -1]]

    for i in range(5):
        try:
            position[0][1] = square[i].index(pair[0])
            position[0][0] = i
        except:
            pass

        try:
            position[1][1] = square[i].index(pair[1])
            position[1][0] = i
        except:
            pass
    
    return position

"""Get the letter pair from polybius square based on given position"""
def get_letters_by_position(square, position):
    result = [square[position[0][0]][position[0][1]], 
              square[position[1][0]][position[1][1]]]
    
    return result

"""Crypt a pair"""
def get_crypted_pair(square, pair):
    result = []
    position = get_positions(square, pair)

    if position[0][0] == position[1][0]:
        result_position = [[position[0][0], (position[0][1] + 1) % 5],
                            [position[1][0], (position[1][1] + 1) % 5]]
        
        result = get_letters_by_position(square, result_position)
    
    elif position[0][1] == position[1][1]:
        result_position = [[(position[0][0] + 1) % 5, position[0][1]],
                            [(position[1][0] + 1) % 5, position[1][1]]]
        
        result = get_letters_by_position(square, result_position)
    else:
        result_position = [[(position[0][0]), position[1][1]],
                            [(position[1][0]), position[0][1]]]
        
        result = get_letters_by_position(square, result_position)

    return result

"""Decrypt a pair"""
def get_decrypted_pair(square, pair):
    result = []
    position = get_positions(square, pair)

    if position[0][0] == position[1][0]:
        result_position = [[position[0][0], (position[0][1] + 4) % 5],
                            [position[1][0], (position[1][1] + 4) % 5]]
        
        result = get_letters_by_position(square, result_position)
    
    elif position[0][1] == position[1][1]:
        result_position = [[(position[0][0] + 4) % 5, position[0][1]],
                            [(position[1][0] + 4) % 5, position[1][1]]]
        
        result = get_letters_by_position(square, result_position)
    else:
        result_position = [[(position[0][0]), position[1][1]],
                            [(position[1][0]), position[0][1]]]
        
        result = get_letters_by_position(square, result_position)

    return result

"""Prepare the massage in order to encrypt/decrypt it"""
def prepare_message(message):
    message_letters = list(re.sub('[^A-Z]', '', message.upper()))

    letter_pairs = []

    count = 0
    last_letter = '-'

    for current_letter in message_letters:
        count += 1
        
        if count == 2:
            if current_letter != last_letter:
                letter_pairs.append([last_letter, current_letter])
            else:
                letter_pairs.append([last_letter, 'X'])

            count = 0
        else:    
            last_letter = current_letter

    if(count == 1):
        letter_pairs.append([last_letter, 'X'])

    return letter_pairs

"""Crypt the message based on given key"""
def crypt(message, key):
    square = get_polybius_square(key)
    prepared_text = prepare_message(message)
    result_list = []

    for pair in prepared_text:
        result_list.append(get_crypted_pair(square, pair))

    result = ""

    for pair in result_list:
        result += pair[0] + pair[1] + ' '

    return result

"""Decrypt the message based on given key"""
def decrypt(message, key):
    square = get_polybius_square(key)
    prepared_text = prepare_message(message)
    result_list = []

    for pair in prepared_text:
        result_list.append(get_decrypted_pair(square, pair))

    result = ""

    for pair in result_list:
        result += pair[0] + pair[1] + ' '

    return result