if __name__ == '__main__':

    nin = input("Insert 4 non-integer numbers: ")
    nin = nin.split()

    try:
        nin = [float(i) for i in nin]
        print(f"Minimum: {min(nin)}\nMaximum: {max(nin)}")

    except ValueError:
        print("Please insert valid values!!")
