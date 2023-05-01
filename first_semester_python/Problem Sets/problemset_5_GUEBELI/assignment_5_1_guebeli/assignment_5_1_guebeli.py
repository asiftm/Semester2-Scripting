if __name__ == '__main__':

    tri = ""
    tri2 = ""
    while tri != "a" and tri2 != "c" and tri != "b" and tri2 != "d":

        tri = input("Choose a triangle (a or b): ").lower
        tri2 = input("Choose a triangle (c or d): ").lower

    ast = ""
    ast2 = ""
    for n in range(0, 11):

        if tri == "a":
            f = 0
            while f <= n:
                ast += "*"
                f += 1
        else:
            f = 11 - n
            while f > 0:
                ast += "*"
                f += -1

        ast += "\n"

        if tri2 == "c":
            f = 0
            while f < 11:
                if f >= n:
                    ast2 += "*"
                else:
                    ast2 += " "
                f += +1
        else:
            f = 0
            while f <= 11:
                if f < 11-n:
                    ast2 += " "
                else:
                    ast2 += "*"
                f += 1

        ast2 += "\n"

    print(f"{ast}\n{ast2}")


