import requests


def add_book(book: dict[str, str]) -> str | None:
    valid = ["mathematics", "physics", "chess"]

    if book["category"] not in valid:
        return "Invalid Category"
        
    if book["category"] == valid[0]:
        url = "http://127.0.0.1:8000/mathematics/"

    elif book["category"] == valid[1]:
        url = "http://127.0.0.1:8000/physics/"

    elif book["category"] == valid[2]:
        url = "http://127.0.0.1:8000/chess/"

    respons = requests.get(url)
    if respons.status_code != 200:
        return "Bad Request"

    data = respons.json()

    for item in data:
        if book["name"] == item["name"]:
            return "Bad Request"

    requests.post(url, json=book)