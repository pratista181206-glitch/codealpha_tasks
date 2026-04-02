import random

WORDS = ["python", "hangman", "coding", "keyboard", "monitor"]

def play():
    word = random.choice(WORDS)
    guessed = set()
    lives = 6

    print("\n====  HANGMAN  ====")
    print(f"Word has {len(word)} letters. You have {lives} lives.\n")

    while lives > 0:
        # Show current word progress
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print(f"Word:  {display}")
        print(f"Lives: {lives}  |  Wrong: {sorted(g for g in guessed if g not in word)}")

        # Check win
        if "_" not in display:
            print("\n🎉 You guessed it! Well done!")
            return

        guess = input("Guess a letter: ").strip().lower()

        # Basic validation
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter only.\n")
            continue
        if guess in guessed:
            print("Already guessed that!\n")
            continue

        guessed.add(guess)

        if guess in word:
            print("✅ Correct!\n")
        else:
            lives -= 1
            print(f"❌ Nope! {lives} lives left.\n")

    print(f"💀 Out of lives! The word was '{word}'.")

# --- Run the game ---
while True:
    play()
    if input("Play again? (y/n): ").strip().lower() != "y":
        print("Bye! 👋")
        break
