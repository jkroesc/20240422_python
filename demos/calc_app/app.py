from typing import Any
from calculate import do_math
import interact as i
import history as h

history = h.History([])


def check_command(cmd: str) -> int:
    commands: list[str] = [
        "add",
        "subtract",
        "multiply",
        "divide",
        "clear",
        "history",
        "remove",
    ]
    for command in commands:
        if cmd == command:
            return 1
    return 0


def print_return(val: float) -> None:
    print(f"Result: {val}")


def print_error(message: str) -> None:
    print(f"Error: {message}")


def main() -> None:
    while True:
        command: str = i.get_command()
        if command == "exit":
            break
        if check_command(command) == 0:
            print_error("Enter a valid command.")
        elif command == "clear":
            history.clear()
        elif command == "history":
            history.print()
        elif command == "remove":
            history.remove()
        else:
            history.add_rec(command)
        print_return(history.get_result())


if __name__ == "__main__":
    main()
