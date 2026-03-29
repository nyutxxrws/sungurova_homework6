def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("А роза упала на лапу Азора") == True
assert is_palindrome("Казак") == True
assert is_palindrome("Мир") == False
assert is_palindrome("12321") == True
print("Все 5 тестов пройдены успешно!")