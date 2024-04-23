def main() -> None:
    while True:
        command = input("Enter a command: ")

        if command == "exit":
            break  # exits the loop

        print(f"Received command: {command}")


if __name__ == "__main__":
    main()
