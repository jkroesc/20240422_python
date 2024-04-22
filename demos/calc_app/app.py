def main() -> None:
    val: int | float = 0
    while True:
        command = input("Please enter a command (or exit): ")
        if command == "exit":
            break
        if command != "clear":
            operand = int(input("Please enter an operand (int): "))

        if command == "add":
            val = val + operand
        elif command == "subtract":
            val = val - operand
        elif command == "multiply":
            val = val * operand
        elif command == "divide":
            val = val / operand
        elif command == "clear":
            val = 0
        else:
            print(
                "Sorry, you have not entered an Ed Sheeran album name. Try again."
            )

        print(val)


if __name__ == "__main__":
    main()
