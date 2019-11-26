def is_palindrome(str):
    rev = reverse(str)
    
    if (str == rev):
        return True
    return False

print(is_palindrome("radar"))
