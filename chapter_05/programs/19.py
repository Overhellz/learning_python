def main():
    choice = int(input('Месяцев: '))
    calc(choice)


def calc(t):
    i = 0.16 / 12
    P = 2500000
    sum = P * ((1 + i) ** t)
    print(sum)


if __name__ == '__main__':
    main()
