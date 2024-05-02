import random

categories = ["Fruit", "Clothing", "Tool"]
category = random.choice(categories)
if category == 'Fruit':
    words = ["apple", "banana", "cherry", "orange", "grape"]
    word = random.choice(words)
elif category == 'Clothing':
    words = ["shirt", "blouse", "pants", "gloves", "socks"]
    word = random.choice(words)
elif category == 'Tool':
    words = ["hammer", "knife", "wrench", "jigsaw", "level"]
    word = random.choice(words)

guessed_letters = ["_"] * len(word)
attempts = 6

print(category)
print(" ".join(guessed_letters))

while attempts > 0 and "_" in guessed_letters:
    guess = input("Enter a letter: ")
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_letters[i] = guess
    else:
        attempts -= 1
        print(f"Incorrect guess. Attempts left: {attempts}")
    
    print(" ".join(guessed_letters))

if "_" not in guessed_letters:
    print("Congratulation! You guessed the word correctly")
else:
    print(f"Out of attempts! The word was : {word}")