import os
from shutil import copyfile


class FileManager:
    del_info = dict()
    def find(self, name: str, address: str) -> list:
        result = list()
        for root, dirs, files in os.walk(address):
            for file in files:
                if file == name:
                    result.append(os.path.join(root, file))
        return result


    def create_file(self, name: str, address: str) -> None:
        path = os.path.join(address, name)

        if os.path.isfile(path):
            return

        with open(path, "w"):
            pass

    def create_dir(self, name: str, address: str) -> None:
        path = os.path.join(address, name)

        if os.path.isdir(path):
            return

        os.mkdir(path)

    def delete(self, name: str, address: str) -> None:
        path = os.path.join(address, name)

        if not os.path.isfile(path):
            return

        with open(path, "r") as f:
            content = f.read()

        if name not in self.del_info:
            self.del_info[name] = list()

        self.del_info[name].append({
            "address": address,
            "content": content
        })

        os.remove(path)

    def restore(self, name: str) -> None:
        if name not in self.del_info:
            return

        if not self.del_info[name]:
            return

        item = self.del_info[name].pop()

        path = os.path.join(item["address"], name)

        with open(path, "w") as f:
            f.write(item["content"])