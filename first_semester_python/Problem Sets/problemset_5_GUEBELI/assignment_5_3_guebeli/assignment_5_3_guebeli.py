if __name__ == '__main__':

    lower = input("Lower bound: ")
    try:
        lower = int(lower)
        upper = lower - 1
        while upper < lower:
            upper = input("Upper bound: ")
            upper = int(upper)

        oddNum = lower + (lower + 1) % 2
        product = oddNum
        while oddNum < upper:
            oddNum = oddNum + 2
            product *= oddNum

        print(product)

    except ValueError:
        print("Insert valid values!")
