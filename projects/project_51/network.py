import socket, json


class Network:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.s.connect((self.host, self.port))
        data = self.s.recv(4096)
        data = data.decode('ascii')
        self.data = json.loads(data)
        with open("config.json", "w") as f:
            json.dump(self.data, f)

    def send_data(self, keys):
        if not keys:
            fi_key = "no_key"

        else:
            fi_key = keys[0]

        join_item = ("snake", str(self.data["id"]), fi_key)
        full_key = "_".join(join_item)

        result = {
            "keys" : [full_key],
            "dead" : False
        }

        finally_result = json.dumps(result)
        finally_result = finally_result.encode('ascii')
        self.s.send(finally_result)

    def get_data(self):
        data = self.s.recv(4096)
        data = data.decode('ascii')
        data = data.replace("'", '"')

        result = json.loads(data)
        return result