def translate_to_braille(text_input):
    braille_dict = {
        'a': '100000', 'b': '110000', 'c': '100100', 'd': '100110', 'e': '100010',
        'f': '110100', 'g': '110110', 'h': '110010', 'i': '010100', 'j': '010110',
        'k': '101000', 'l': '111000', 'm': '101100', 'n': '101110', 'o': '101010',
        'p': '111100', 'q': '111110', 'r': '111010', 's': '011100', 't': '011110',
        'u': '101001', 'v': '111001', 'w': '010111', 'x': '101101', 'y': '101111', 
        'z': '101011', ' ': '000000'

        # Add these right into your existing braille_dict:
'.': '001011', ',': '010000', '!': '011010', '?': '011001', '-': '001001'
    }
    
    # Braille maps numbers 1-9 and 0 to the letters a-j
    num_dict = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
        '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
    }
    
    final_output = ""
    
    for character in text_input:
        # Rule 1: Handle Capital Letters
        if character.isupper():
            final_output += "000001"  # Capital indicator
            final_output += braille_dict[character.lower()]
            
        # Rule 2: Handle Numbers
        elif character.isdigit():
            final_output += "001111"  # Number indicator
            corresponding_letter = num_dict[character]
            final_output += braille_dict[corresponding_letter]
            
        # Rule 3: Handle Known Lowercase Letters and Spaces
        elif character in braille_dict:
            final_output += braille_dict[character]
            
        # Rule 4: Safely Ignore Unknown Punctuation (Prevents Crashing)
        else:
            continue 
            
    return final_output

print(translate_to_braille("a A 1"))
