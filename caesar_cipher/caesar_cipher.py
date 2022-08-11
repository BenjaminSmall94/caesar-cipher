import re
from caesar_cipher.corpus_loader import word_list, name_list


def encrypt(plain_text, shift):
    def do_shift(curr_char, shift, max_ord):
        new_ord = ord(curr_char) + (shift % 26)
        if new_ord > max_ord:
            return new_ord - 26
        return new_ord

    cipher_text = ""
    for char in plain_text:
        if 65 <= ord(char) <= 90:
            cipher_text += chr(do_shift(char, shift, 90))
        elif 97 <= ord(char) <= 122:
            cipher_text += chr(do_shift(char, shift, 122))
        else:
            cipher_text += char
    return cipher_text


def decrypt(cipher_text, shift):
    return encrypt(cipher_text, -shift)


def crack(cipher_text):
    def get_english_word_count(shifted_text_list):
        word_count = 0
        for candidate in shifted_text_list:
            stripped_candidate = re.sub(r"[^A-Za-z']+",'', candidate)
            if stripped_candidate.lower() in word_list or stripped_candidate in name_list:
                word_count += 1
        return word_count

    def test_shift(shifted_text_list):
        english_word_count = get_english_word_count(shifted_text_list)
        percentage = int(english_word_count / len(shifted_text_list) * 100)
        if percentage > 50:
            return True

    for shift_num in range(26):
        shifted_text = decrypt(cipher_text, shift_num)
        shifted_text_list = shifted_text.split()
        if test_shift(shifted_text_list):
            return shifted_text
