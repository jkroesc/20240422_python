def get_operand() -> float:
    return_val: float = 0.0
    user_input: str = ""
    while user_input == "":
        try:
            user_input = input("Please enter an operand: ")
            return_val = float(user_input)
        except Exception:
            print("Invalid data type. Please enter an operand: ")
            user_input = ""
    return return_val


def get_command() -> str:
    return input("Please enter a command (or exit): ")


def get_delete_index() -> int:
    del_index: int = 0
    while True:
        try:
            del_index = int(input("Enter the index to remove: "))
            break
        except Exception:
            print("Invalid entry.")
    return del_index
