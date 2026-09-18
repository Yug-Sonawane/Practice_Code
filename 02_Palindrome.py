# Palindrome.py 

#user data

data = input("Enter your multiple words: ").split()

for word in data:
    if word[::-1]==word:
        print(word, "is palindrome")

    else:
        print(word, "is not palindrome")