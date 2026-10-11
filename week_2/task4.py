print("=====PALINDROME CHECKER===")
word = input("Enter a word: ")
word = word.lower()  # Convert the word to lowercase for case-insensitive comparison
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

print("===========================")