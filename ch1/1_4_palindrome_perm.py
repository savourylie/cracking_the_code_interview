def palindrome_perm(string):
    if len(string) == 0 or len(string) == 1:
        return True

    string = string.lower()
    string = string.replace(' ', '')
    char_dict = {}

    for i, x in enumerate(string):
            char_dict[x] = char_dict.get(x, 0) + 1

    if len(string) % 2 == 0:
        for key, value in char_dict.items():
            if value % 2 != 0:
                return False
    else:
        count = 0
        for key, value in char_dict.items():
            if value % 2 != 0:
                count += 1

                if count > 1:
                    return False

    return True


if __name__ == '__main__':
    assert palindrome_perm('Tact Coa')
    assert not palindrome_perm('Tact Coaa')
    assert palindrome_perm('Civic')
    assert not palindrome_perm('apple')
    assert palindrome_perm('lol')
    assert palindrome_perm('llo')
    assert palindrome_perm('lolo')
    assert not palindrome_perm('aaabbbc')
    print("All tests passed.")