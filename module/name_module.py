def ispallindrome(name):
    if name == name[::-1]:
        return True
    return False


def count_the_vowels(name):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in name:
        if ch in vowels:
            count += 1

    return count


def frequency_of_letters(name):
    freq = {}

    for ch in name:
        freq[ch] = freq.get(ch, 0) + 1

    return freq