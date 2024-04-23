def main() -> None:  # "-> None" indicates a return type.
    print("Hello, World!")


# files are modules and modules are files. These can be an executable or library
# exec: "python ./app.py", and __name__ == __main__
# lib: import app

# This is a guard. It only runs the code when the file is used as an executable.
if __name__ == "__main__":
    print("app")
    main()

# If the guard is not there, all methods are run when the file main method is called.
