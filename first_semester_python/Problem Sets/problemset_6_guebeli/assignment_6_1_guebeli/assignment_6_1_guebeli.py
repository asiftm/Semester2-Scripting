

if __name__ == '__main__':

    vector = input("Insert a vector (values divided by spaces): ")
    vector = vector.split()
    vector = [float(i) for i in vector]

    multiplier = input("Insert a multiplier: ")
    multiplier = float(multiplier)

    print(f"Multiplication value: {multiplier}\n")
    print(f"Multiplied vector:\n{vector[0]*multiplier}\n{vector[1]*multiplier}\n{vector[2]*multiplier}\n")
    print(f"Original vector:\n{vector[0]}\n{vector[1]}\n{vector[2]}")
