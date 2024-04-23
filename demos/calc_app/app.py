from typing import Any


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


def get_operand() -> float:
    return float(input("Please enter an operand: "))


def do_math(val: float, cmd: str, op: float) -> float:
    if cmd == "add":
        return val + op
    elif cmd == "subtract":
        return val - op
    elif cmd == "multiply":
        return val * op
    elif cmd == "divide":
        return val / op
    else:
        return 0


def main() -> None:
    val: int | float = 0.0
    history_vals: list[dict[str, Any]] = []
    history_index: int = 1

    while True:
        command = input("Please enter a command (or exit): ")
        if command == "exit":
            break

        if check_command(command) == 0:
            print("Enter a valid command.")

        if command == "clear":
            history_index = 0
            history_vals = []
            val = 0
        elif command == "history":
            for h1 in history_vals:
                print(h1)
        elif command == "remove":
            del_val: int = int(
                input("Enter the id for the history to be removed: ")
            )
            for h2 in history_vals:
                if h2["id"] == del_val:
                    history_vals.remove(h2)
                    break
        else:
            operand = get_operand()
            val = do_math(val, command, operand)
            history_vals.append(
                {
                    "id": history_index,
                    "command": command,
                    "operand": operand,
                }
            )
            history_index += 1
            print(f"Result: {val}")


if __name__ == "__main__":
    main()
