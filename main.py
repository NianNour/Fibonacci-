"""fibonacci series."""

def main():
    """ the main function. """
    first_sent = 0
    second_sent = 1
    fibo_series = "0, 1"
    answer = 0
    #number = int(input("enter the number of sentance.."))

    while True:
        try:
            number = int(input("enter the number of sentance: "))
            if number<0:
                raise ValueError(" Number must be greater than 0! Try again...")
            break
        except ValueError as error:
            print(error)

    for i in range(number):
        answer = first_sent + second_sent
        first_sent = second_sent
        second_sent = answer
        fibo_series = fibo_series + ", "+str(answer)
    print(fibo_series)


if __name__ == "__main__":
    main()
