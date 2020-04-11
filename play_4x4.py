board = ["-", "-", "-", "-",
         "-", "-", "-", "-",
         "-", "-", "-", "-",
         "-", "-", "-", "-",
         ]


class Game4x4(object):

    # sprawdzanie kolumn
    def column(self):

        for nr_column in range(4):

            o = 0
            x = 0

            for unit in range(4):

                if board[(unit * 4) + nr_column] == "o":
                    o += 1

                if board[(unit * 4) + nr_column] == "x":
                    x += 1

                if (o > 1) and (x > 1):
                    break

            if o == 4:
                print("Player1 wins")
                quit()

            if x == 4:
                print("Player2 wins")
                quit()


    # sprawdzanie wierszy
    def rows(self):

        for nr_rows in range(4):

            o = 0
            x = 0

            for unit in range(4):

                if board[unit + (nr_rows * 4)] == "o":
                    o += 1

                if board[unit + (nr_rows * 4)] == "x":
                    x += 1

                if (o > 1) and (x > 1):
                    break

            if o == 4:
                print("Player1 wins")
                quit()

            if x == 4:
                print("Player2 wins")
                quit()

    # sprawdzanie skosow
    def slant(self):

        x = 0
        o = 0

        x2 = 0
        o2 = 0

        for i in range(4):

            if board[i + (i * 4)] == "o":
                o += 1

            if board[i + (i * 4)] == "x":
                x += 1

            if (o > 1) and (x > 1):
                break

        for j in range(3, 7, 3):

            if board[j] == "o":
                o2 += 1

            if board[j] == "x":
                x2 += 1

            if (o2 > 1) and (x2 > 1):
                break

        if o == 4 or o2 == 4:
            print("Player1 wins")
            quit()

        if x == 4 or x2 == 4:
            print("Player2 wins")
            quit()

    # sprawdzanie kwadratow
    def square(self):
        for k in range(3):

            for i in range(3):
                o = 0
                x = 0

                for j in range(2):
                    if board[j + i + (4 * k)] == "o":
                        o += 1

                    if board[j + 4 + i + (4 * k)] == "o":
                        o += 1

                    if board[j + i + (4 * k)] == "x":
                        x += 1

                    if board[j + 4 + i + (4 * k)] == "x":
                        x += 1

                    if (o > 1) and (x > 1):
                        break

                if o == 4:
                    print("Player1 wins")
                    quit()

                if x == 4:
                    print("Player2 wins")
                    quit()


    # ogolna funkcja sprawdzajaca wszystkie mozliwosci
    def check(self, column, rows, slant, square):
        column()
        rows()
        slant()
        square()
