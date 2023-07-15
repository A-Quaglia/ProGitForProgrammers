
lifes   = ("[ ] [ ] [ ] [ ] [ ] [ ]",
           "[X] [ ] [ ] [ ] [ ] [ ]",
           "[X] [X] [ ] [ ] [ ] [ ]",
           "[X] [X] [X] [ ] [ ] [ ]",
           "[X] [X] [X] [X] [ ] [ ]",
           "[X] [X] [X] [X] [X] [ ]",
           "[X] [X] [X] [X] [X] [X]")

class Hangman:
    def __init__(self, word="test"):
        self.result = word.upper()
        self.lifes = lifes
        self.errors = 0
        self.attempts = 0
        self.word = ["_"]*len(self.result)
        self.gameon = True

        self.game_loop()

    def print_board(self):
        print(self.lifes[self.errors])
        print(f"Attempts: {self.attempts}.")
        print(" ".join(self.word))

    def get_input(self):
        new_letter = input("| Enter a new letter:").upper()
        if new_letter in self.result:
            for i, letter in enumerate(self.result):
                if letter == new_letter:
                    self.word[i] = letter
        else:
            self.errors += 1

    def test_game_over(self):
        if self.word.count("_") == 0:
            print(" ".join(self.word))
            print("YOU WON")
            self.gameon = False
        elif self.errors == 6:
            print(" ".join(self.word))
            print("GAME OVER")
            print(f"The word was: {self.result}")
            self.gameon = False

    def game_loop(self):
        for i, letter in enumerate(self.result):
                if letter == " ":
                    self.word[i] = letter
        while self.gameon:
            self.print_board()
            self.get_input()
            self.test_game_over()



if __name__ == "__main__":
    Hangman("Choque de Cultura")