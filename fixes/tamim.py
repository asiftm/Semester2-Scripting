import string


def f():
    sonnet = open("sonnets.txt", "r")

    my_list = sonnet.read().lower().replace("\n", " ").split(" ")

    u_list = [x.strip() for x in my_list]

    for i in range(len(u_list)):
        u_list[i] = u_list[i].replace(',', '').replace(':', '').replace('‘', '').replace('.', '').replace('!',
                                                                                                          '').replace(
            '?', '').replace('(', '').replace(')', '').replace('" "', '').replace("'", '')

        new_list = [string for string in u_list if string != '']

    sorted_words = sorted(new_list)
    print(sorted_words)
    # count_and = sorted_words.count("and")
    #
    # print(f"and {count_and}")
    #
    # count_time = sorted_words.count("time")
    #
    # print(f"time {count_time}")
    #
    # count_as = sorted_words.count("as")
    #
    # print(f"as {count_as}")
    #
    # count_my = sorted_words.count("my")
    #
    # print(f"my {count_my}")
    #
    # print(sorted_words)


def main():
    f()


if __name__ == "__main__":
    main()
