def main():
    choice = int(input('Время падения: '))
    g = 9.8
    d = 0.5 * g * (choice ** 2)
    print(f'{choice} s\t= {d} m')


if __name__ == '__main__':
    main()
