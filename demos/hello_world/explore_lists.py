from typing import Any


def main() -> None:
    nums = [1, 2, 3, 4, 5]
    letters = ["a", "b", "c", "d", "e"]
    people: list[dict[str, Any]] = [
        {"name": "Bob", "age": 23},
        {"name": "Mary", "age": 29},
    ]

    for num in nums:
        print(num)

    for person in people:
        print(person["name"], person["age"])


if __name__ == "__main__":
    main()
