from calculate import do_math
import interact as i


class Entry:
    def __init__(
        self,
        entry: dict,
        id: int,
        command: str,
        operand: float,
    ) -> None:
        self.id = id
        self.command = command
        self.operand = operand
        self.entry = {
            "id": id,
            "command": command,
            "operand": operand,
        }


class History:
    def __init__(
        self,
        history: list,
    ) -> None:
        self.history = history

    def get_next_id(self) -> int:
        return len(self.history) + 1

    def append(self, cmd: str, op: float) -> None:
        self.history.append(
            {
                "id": self.get_next_id(),
                "command": cmd,
                "operand": op,
            }
        )

    def clear(self) -> None:
        self.history.clear()

    def remove(self) -> None:
        del_index: int = i.get_delete_index()
        if del_index in range(len(self.history)):
            del self.history[del_index]

    def print(self) -> None:
        for rec in self.history:
            print(
                f"{self.history.index(rec)}: {rec['command']} {rec['operand']}"
            )

    def add_rec(self, cmd: str) -> None:
        self.history.append({"command": cmd, "operand": i.get_operand()})

    def get_result(self) -> float:
        ret: float = 0.0
        for h in self.history:
            ret = do_math(ret, h["command"], h["operand"])
        return ret
