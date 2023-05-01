
if __name__ == '__main__':

    numbers = []

    while True:
        try:
            number = int(input("Insert an integer number: "))
        except ValueError:
            print("Please insert valid numbers!")
        else:
            if number != 0:
                numbers.append(number)
            else:
                break

    positive = 0
    negative = 0

    for i in numbers:
        if i >= 0:
            positive += 1
        else:
            negative += 1

    print(f"\nSum: {sum(numbers)}\nMean: {sum(numbers)/len(numbers)}\n\n"
          f"Positive numbers: {positive} ({int((positive/len(numbers))*100)}%)\n"
          f"Negative numbers: {negative} ({int((negative/len(numbers))*100)}%)")
