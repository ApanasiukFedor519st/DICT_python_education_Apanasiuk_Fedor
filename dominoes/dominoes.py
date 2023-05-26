import random


class Dominoes:
    def __init__(self):
        self.dominoes = [[0, 0],
                         [0, 1], [1, 1],
                         [0, 2], [1, 2], [2, 2],
                         [0, 3], [1, 3], [2, 3], [3, 3],
                         [0, 4], [1, 4], [2, 4], [3, 4], [4, 4],
                         [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5],
                         [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6]
                         ]
        self.player = []
        self.computer = []
        self.stock = []
        self.snake = []
        self.status = ""
        self.turn = 0
        self.rating = []
        self.max_points = -1
        self.dom_pos = None
        self.current_element = None


    def creat(self):

        dominoes = self.dominoes.copy()


        for piece in range(7):
            self.player.append(random.choice(dominoes))
            dominoes.remove(self.player[piece])
            self.computer.append(random.choice(dominoes))
            dominoes.remove(self.computer[piece])
        self.stock = dominoes.copy()
        game.game_rules()


    def game_rules(self):


        for i in range(7):
            if self.player[i][0] == self.player[i][1]:
                self.snake.append(self.player[i])
                self.player.remove(self.player[i])
                self.status = "Computer is about to make a move. Press Enter to continue..."
                self.turn = 1
                game.get_screen()
                break

            elif self.computer[i][0] == self.computer[i][1]:
                self.snake.append(self.computer[i])
                self.computer.remove(self.computer[i])
                self.status = "It's your turn to make a move. Enter your command."
                self.turn = 0
                game.get_screen()
                break


            else:
                game.__init__()
                game.creat()
                break


    def switch(self):
        if self.turn == 0:
            self.turn = 1
            self.status = "Computer is about to make a move. Press Enter to continue..."
        elif self.turn == 1:
            self.turn = 0
            self.status = "It's your turn to make a move. Enter your command."

    def get_players(self):
        while True:

            dom_pos = input("> ")


            if (dom_pos.isdigit() or '-' in dom_pos and dom_pos.strip('-')) \
                    and int(dom_pos) in range(-len(self.player), len(self.player) + 1):


                dom_pos = int(dom_pos)


                if dom_pos < 0:

                    dom_pos = abs(dom_pos)


                    if self.player[dom_pos - 1][1] == self.snake[0][0]:
                        self.snake.insert(0, self.player[dom_pos - 1])
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    elif self.player[dom_pos - 1][0] == self.snake[0][0]:
                        rev = list(self.player[dom_pos - 1])
                        rev.reverse()
                        self.snake.insert(0, rev)
                        self.player.remove(self.player[dom_pos - 1])
                        break


                    else:
                        print("Illegal move. Please try again.")


                elif dom_pos > 0:


                    if self.player[dom_pos - 1][1] == self.snake[-1][1]:
                        rev = list(self.player[dom_pos - 1])
                        rev.reverse()

                        self.snake.append(rev)
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    elif self.player[dom_pos - 1][0] == self.snake[-1][1]:
                        self.snake.append(self.player[dom_pos - 1])
                        self.player.remove(self.player[dom_pos - 1])
                        break


                    else:
                        print("Illegal move. Please try again.")


                elif dom_pos == 0:
                    self.player.append(random.choice(self.stock))
                    self.stock.remove(self.player[-1])
                    break
            else:
                print("Invalid input. Please try again.")

    def rate_and_input(self):
        for element in self.rating:

            if element[2] == self.max_points:
                self.dom_pos = element[0]
                self.current_element = element
                break

            elif element[2] != self.max_points and self.rating[-1] == element:
                self.max_points -= 1
                game.rate_and_input()

    def get_rating(self):
        self.rating.clear()
        self.current_element = None
        numbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

        for key1, elem in enumerate(self.computer):
            for num in elem:
                numbers[num] += 1

        for key, element in enumerate(self.computer):
            points = numbers.get(element[0]) + numbers.get(element[1])
            self.rating.append([key, element, points])

            if points > self.max_points:
                self.max_points = points

    def compare_inp(self):
        while True:
            game.rate_and_input()

            if self.computer[self.dom_pos - 1][1] == self.snake[0][0]:
                self.snake.insert(0, self.computer[self.dom_pos - 1])
                self.computer.remove(self.computer[self.dom_pos - 1])
                break

            elif self.computer[self.dom_pos - 1][0] == self.snake[0][0]:
                rev = list(self.computer[self.dom_pos - 1])
                rev.reverse()
                self.snake.insert(0, rev)
                self.computer.remove(self.computer[self.dom_pos - 1])
                break

            elif self.computer[self.dom_pos - 1][1] == self.snake[-1][1]:
                rev = list(self.computer[self.dom_pos - 1])
                rev.reverse()
                self.snake.append(rev)
                self.computer.remove(self.computer[self.dom_pos - 1])
                break

            elif self.computer[self.dom_pos - 1][0] == self.snake[-1][1]:
                self.snake.append(self.computer[self.dom_pos - 1])
                self.computer.remove(self.computer[self.dom_pos - 1])
                break


            elif len(self.rating) == 0:
                self.computer.append(random.choice(self.stock))
                self.stock.remove(self.computer[-1])
                break

            else:
                print(self.max_points)
                print(self.rating)
                self.rating.remove(self.current_element)
                pass


    def get_screen(self):
        print("=" * 70)
        print(f"""Stock size: {len(self.stock)}
Computer pieces: {len(self.computer)}\n""")

        if len(self.snake) > 6:
            print(*self.snake[0:3], "...", *self.snake[len(self.snake) - 3:], sep="")
        else:
            print(*self.snake)

        print("\nYour pieces:")
        for key, elem in enumerate(self.player):
            print(key + 1, ":", elem, sep="")

        print(f"\nStatus: {self.status}")


    def res_anal(self):
        if len(self.computer) == 0:
            return -1
        if len(self.player) == 0:
            return 1


        if len(self.snake) - 2 == 8:
            correctness = True

            for key, element in enumerate(self.snake):
                if element[0] != self.snake[key - 1][1] and key >= 1:
                    correctness = False


            if self.snake[0][0] == self.snake[-1][1] and correctness is True:
                return 0


def get_menu_body():
    game.creat()

    while True:


        if game.turn == 0:
            game.get_players()

        elif game.turn == 1:
            while True:
                action = input("> ")
                if action == "":
                    game.get_rating()
                    game.compare_inp()
                    break
                else:
                    print("Press Enter")


        if game.res_anal() == 1:
            game.status = "The game is over. You won!\n"
            game.get_screen()
            break
        elif game.res_anal() == -1:
            game.status = "The game is over. The computer won!\n"
            game.get_screen()
            break
        elif game.res_anal() == 0:
            game.status = "The game is over. It's a draw!\n"
            game.get_screen()
            break

        game.switch()
        game.get_screen()

    Start_menu()


def Start_menu():
    game.__init__()
    action = input("""1. Play
0. Exit\n""")

    if action == '1':
        get_menu_body()
    elif action == '0':
        pass
    else:
        Start_menu()


if __name__ == "__main__":
    game = Dominoes()
    Start_menu()