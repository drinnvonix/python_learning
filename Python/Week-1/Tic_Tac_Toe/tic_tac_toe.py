class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [" "] * 9
        self.current_player = player1

    def reset_board(self):
        self.board = [" "] * 9
        self.current_player = self.player1

    def display_board(self):
        print()
        print("     |     |")
        print(f"  {self.board[0]}  |  {self.board[1]}  |  {self.board[2]}")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.board[3]}  |  {self.board[4]}  |  {self.board[5]}")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}")
        print("     |     |")
        print()

    def make_move(self):
        while True:
            try:
                position = int(
                    input(
                        f"{self.current_player.name} "
                        f"({self.current_player.symbol}), "
                        "choose a position (1-9): "
                    )
                )

                if position < 1 or position > 9:
                    print("Please choose a number between 1 and 9.")
                    continue

                index = position - 1

                if self.board[index] != " ":
                    print("That position is already occupied.")
                    continue

                self.board[index] = self.current_player.symbol
                break

            except ValueError:
                print("Please enter a valid number.")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for combination in winning_combinations:
            if (
                self.board[combination[0]] == self.current_player.symbol
                and self.board[combination[1]] == self.current_player.symbol
                and self.board[combination[2]] == self.current_player.symbol
            ):
                return True

        return False

    def check_draw(self):
        return " " not in self.board

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play_round(self):
        self.reset_board()

        while True:
            self.display_board()

            self.make_move()

            if self.check_winner():
                self.display_board()

                print(
                    f"🎉 {self.current_player.name} "
                    f"({self.current_player.symbol}) wins!"
                )

                self.current_player.score += 1
                break

            if self.check_draw():
                self.display_board()
                print("It's a draw!")
                break

            self.switch_player()


def get_player_details(player_number, used_symbol=None):

    print(f"\nPlayer {player_number}")

    name = input("Enter player name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter player name: ").strip()

    while True:
        symbol = input("Choose your symbol: ").strip()

        if symbol == "":
            print("Symbol cannot be empty.")
            continue

        if len(symbol) != 1:
            print("Please choose only one character.")
            continue

        if symbol == used_symbol:
            print("That symbol is already being used.")
            continue

        break

    return Player(name, symbol)


def display_score(player1, player2):
    print(f"{player1.name} ({player1.symbol}) : {player1.score}")
    print(f"{player2.name} ({player2.symbol}) : {player2.score}")


def main():

    print("       TIC-TAC-TOE GAME")

    player1 = get_player_details(1)

    player2 = get_player_details(
        2,
        player1.symbol
    )

    game = Game(player1, player2)

    while True:

        print("\n GAME MENU ")
        print("1. Start Game")
        print("2. Show Score")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:

            case "1":

                game.play_round()

                display_score(player1, player2)

                while True:
                    play_again = input(
                        "\nDo you want to play again? (y/n): "
                    ).strip().lower()

                    if play_again == "y":
                        break

                    elif play_again == "n":
                        print("\nThanks for playing!")
                        return

                    else:
                        print("Please enter y or n.")

            case "2":
                display_score(player1, player2)

            case "3":
                print("\nThanks for playing!")
                break

            case _:
                print("Invalid choice. Please choose 1, 2, or 3.")


main()