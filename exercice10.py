def estPalindrome(mot):
    i = 0
    mot = mot.lower()
    while i < len(mot) // 2:
        if mot[i] != mot[len(mot) - (i + 1)]:
            return False
        i += 1
    return True

mot = input("Tapez un mot : ")
if estPalindrome(mot):
    print("Oui, c'est un palindrome.")
else: 
    print("Non, ce n'est pas un palindrome.")
