import json

from src.my_module import get_greeting


def main() -> None:
    greeting = get_greeting("Alice")
    data = {
        "greeting": greeting,
    }
    with open("data.json", mode="w", encoding="utf-8") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
