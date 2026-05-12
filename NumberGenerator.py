import random
import os


class NumberGuessingGame:
    def __init__(self):
        self.high_score = self.load_high_score()
        self.max_number = 100
        self.attempts = 7
        self.difficulty_multiplier = 1

    def load_high_score(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as file:
                return int(file.read())
        return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def choose_difficulty(self):
        print("\nSelect Difficulty:")
        print("1) Easy   (1–50  | 10 attempts)")
        print("2) Medium (1–100 | 7 attempts)")
        print("3) Hard   (1–200 | 5 attempts)")

        while True:
            choice = input("Choice (1/2/3): ")

            if choice == "1":
                self.max_number = 50
                self.attempts = 10
                self.difficulty_multiplier = 1
                break
            elif choice == "2":
                self.max_number = 100
                self.attempts = 7
                self.difficulty_multiplier = 2
                break
            elif choice == "3":
                self.max_number = 200
                self.attempts = 5
                self.difficulty_multiplier = 3
                break
            else:
                print("Invalid choice. Try again.")

    def get_valid_guess(self):
        while True:
            guess = input("Enter your guess (or 'q' to quit): ")

            if guess.lower() == "q":
                return None

            try:
                guess = int(guess)
                if 1 <= guess <= self.max_number:
                    return guess
                else:
                    print(f"Enter a number between 1 and {self.max_number}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def give_hint(self, difference):
        if difference == 0:
            return
        elif difference <= 3:
            print("🔥 Extremely hot!")
        elif difference <= 7:
            print("🌡 Very warm!")
        elif difference <= 15:
            print("🙂 Warm.")
        else:
            print("❄ Cold.")

    def play(self):
        self.choose_difficulty()
        secret_number = random.randint(1, self.max_number)
        attempts_left = self.attempts
        base_score = attempts_left * 10

        print(f"\nGuess a number between 1 and {self.max_number}!")

        while attempts_left > 0:
            print(f"\nAttempts left: {attempts_left}")
            guess = self.get_valid_guess()

            if guess is None:
                print("Exiting game...")
                return None

            difference = abs(secret_number - guess)

            if guess == secret_number:
                final_score = base_score * self.difficulty_multiplier
                print("\n🎉 CORRECT! You guessed the number!")
                print(f"⭐ Your score: {final_score}")

                if final_score > self.high_score:
                    self.high_score = final_score
                    self.save_high_score()
                    print("🏆 NEW HIGH SCORE!")

                return final_score

            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

            self.give_hint(difference)

            attempts_left -= 1
            base_score -= 10

        print(f"\n💀 Game Over! The number was {secret_number}.")
        return 0


def main():
    game = NumberGuessingGame()

    while True:
        print("\n==============================")
        print("   NUMBER GUESSING GAME PRO")
        print("==============================")
        print(f"🏆 High Score: {game.high_score}")

        game.play()

        replay = input("\nPlay again? (y/n): ")
        if replay.lower() != "y":
            print("\nThanks for playing! 🚀")
            break


if __name__ == "__main__":
    main()