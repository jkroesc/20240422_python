def main() -> None:
    person = {"first_name": "Bob", "last_name": "Smith", "age": 23}

    print(person["first_name"])
    print(person["last_name"])
    print(person["age"])
    print(person)

    person["middle_name"] = "John"
    for key in person:
        print(person[key])

    try:
        print(person["pet_name"])
    except KeyError:
        print("KeyError: pet_name")

    print(person.get("pet_name", "N/A"))

    del person["middle_name"]
    print(person)


if __name__ == "__main__":
    main()
