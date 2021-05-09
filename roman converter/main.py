from calc import Calculator

def main():
    the_num = input("Enter your value: ")
    calc = Calculator(int(the_num))
    print(calc.make_roman())


if __name__ == '__main__':
    main()

