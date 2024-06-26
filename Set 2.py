def shift_letter(letter, shift):
    if letter == " ":
        return " "
        
    original_position = ord(letter) - ord('A')
    new_position = (original_position + shift) % 26
    new_letter = chr(new_position + ord('A'))
    
    return new_letter

shift_letter(" ", 2)