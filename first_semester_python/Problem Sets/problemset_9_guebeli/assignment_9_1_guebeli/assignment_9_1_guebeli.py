def rec_pi(limit, num=1, pi=0):
    pi += 4 / num
    if num > 0:
        num += 2
    else:
        num -= 2
    if limit == 0:
        return pi
    else:
        return rec_pi(limit-1, num*-1, pi)


if __name__ == '__main__':
    print(rec_pi(43))


