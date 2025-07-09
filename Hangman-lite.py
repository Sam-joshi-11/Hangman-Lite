import random

words = ["banana", "elephant", "apple", "guitar", "python"]
secret_word = random.choice(words)
guessed_letters = []
lives = 6

print("🎯 Welcome to Hangman Lite!")
print("_ " * len(secret_word))

while lives > 0:
    guess = input("🔤 Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        lives -= 1
        print(f"❌ Wrong! Lives left: {lives}")

    # Show current word status
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter 
        else:
            display += "_ "
    print(display)

    # Check win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 You guessed it right! The word was:", secret_word)
        break

if lives == 0:
    print("💀 Game Over! The word was:", secret_word)