import requests


def find_category(url: str) -> str:
    try:
        params = {"name" : "ALL", "category" : "ALL"}
        respons = requests.get(url, params=params)
        data = respons.json()
        
        if respons.status_code != 200:
            return "Bad Request"

        if not data:
            return "I can't recognize it"
        
        matchs = 0
        word = data[0]["category"]
        for i in range(len(data)):
            if data[i]["category"] == word:
                matchs += 1

        if matchs == len(data):
            return data[0]["category"]

        if matchs != len(data):
            return "I can't recognize it"


    except:
        return "Bad Request"
        
