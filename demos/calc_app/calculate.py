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
