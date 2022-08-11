import pytest
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack


def test_shift_one():
    actual = encrypt("abcde", 1)
    expected = "bcdef"
    assert actual == expected


def test_shift_10():
    actual = encrypt("acdef", 10)
    expected = "kmnop"


def test_shift_27():
    actual = encrypt("acdefz", 27)
    expected = "bdefga"


def test_shift_one_with_upper():
    actual = encrypt("aBcDe", 1)
    expected = "bCdEf"
    assert actual == expected


def test_shift_with_non_alphas():
    actual = encrypt("1aB cD\n", 2)
    expected = '1cD eF\n'
    assert actual == expected


def test_decrypt():
    expected = "It was the best of times, it was the worst of times."
    encrypted = encrypt(expected, 8)
    actual = decrypt(encrypted, 8)
    assert actual == expected


@pytest.mark.skip("TODO")
def test_crack_8():
    expected = "It was the best of times, it was the worst of times."
    encrypted = encrypt(expected, 8)
    actual = crack(encrypted)
    assert actual == expected


@pytest.mark.skip("TODO")
def test_crack_28():
    expected = "It was the best of times, it was the worst of times."
    encrypted = encrypt(expected, 28)
    actual = crack(encrypted)
    assert actual == expected


def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected


def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected


def test_encrypt_shift_20():
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected


def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected


def test_with_whitespace():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected


def test_with_non_alpha():
    actual = encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    assert actual == expected


def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected


@pytest.mark.skip("TODO")
def test_crack_phrase():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = phrase
    assert actual == expected


@pytest.mark.skip("TODO")
def test_crack_nonsense():
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = ""
    assert actual == expected
