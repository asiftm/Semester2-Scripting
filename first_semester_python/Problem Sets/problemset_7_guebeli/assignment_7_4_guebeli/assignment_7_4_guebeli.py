import time

if __name__ == '__main__':

    factorials = {}

    while True:
        n = int(input("Calculate factorial: "))
        start_time = time.time()
        if n not in factorials:
            fact = 1

            for i in range(1, n + 1):
                fact = fact*i

            factorials[n] = fact
        elif n == "-1":
            break
        else:
            fact = factorials[n]
        final_time = time.time() - start_time

        print(f"Result of {n}! is {fact}.")
        print(f"Time {final_time} ms!")




