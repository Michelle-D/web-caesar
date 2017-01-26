def alphabet_position(letter):
    if len(letter) != 1:
        return 0
    new = ord(letter)
    if 65 <= new <= 90:
        return new - 65
    elif 97 <= new <=122:
        return new - 97
    return 0


def rotate_character(char, rot):
    low_abc = 'abcdefghijklmnopqrstuvwxyz'
    up_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char.isalpha():
        curr_char_pos = int(alphabet_position(char))
        rot_char_pos = int((curr_char_pos + int(rot)) % 26)
        if char.islower():
            rot_char = low_abc[rot_char_pos]
        else:
            rot_char = up_abc[rot_char_pos]
        return rot_char
    else:
        if not char.isalpha():
            return char

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        if char == '':
            encrypted = encrypted + ''
        else:
            rotated_char = rotate_character(char, rot)
            encrypted += rotated_char
    return encrypted
