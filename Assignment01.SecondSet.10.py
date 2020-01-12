number = int(input("Enter a number: "))
#getting the palindrome
def NumberPalindrome (number2):
    Palindrome = 0
    while (number2 != 0):
            LastDigit = number2 % 10
            Palindrome = Palindrome * 10 + LastDigit
            number2 = number2 // 10
    return Palindrome

def ShowThePalindrome (number):
    Palindrome = NumberPalindrome(number)
    print ("Its palindrome is: ",Palindrome)

ShowThePalindrome (number)
