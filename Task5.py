#Програма приймає число та повідомляє чи є воно паліндромом
# (тобто дзеркальним, наприклад 35653 - паліндром, а 35654 - ні)

def palindrome(s):
    return s[::-1] == s

while True:
    s = input("Enter a palindrome: ")
    print(f"{s} is palindrome!" if palindrome(s) else "not a palindrome")