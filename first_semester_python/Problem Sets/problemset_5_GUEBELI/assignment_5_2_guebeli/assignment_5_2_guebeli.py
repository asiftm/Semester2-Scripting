
if __name__ == '__main__':

    divisor = -3
    pi = 4.0
    print("Iter #\tpi")
    print("0\t4.0")
    for i in range(1, 35):
        pi = pi+(4/divisor)
        print(f"{i}\t{pi}")
        divisor = (abs(divisor)+2)*((divisor/abs(divisor))*-1)

