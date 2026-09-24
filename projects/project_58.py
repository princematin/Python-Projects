import re

class Security:

    def secure(self, info: str) -> str:
        pattern = r"[A-Z][A-Za-z]+:www\.[a-z0-9.]+\.[a-z0-9]+/[A-Za-z0-9_]+"
        for match in re.finditer(pattern, info):
            account = match.group()

            result = account.split("/")
            result[1] = self.encrypt(result[1])
            n_acc = "/".join(result)
            info = info.replace(account, n_acc)
        return info

    def is_social_account_info(self, param: str) -> bool:
        pattern = r"[A-Z][A-Za-z]+:www\.[a-z0-9.]*\.[a-z0-9.]+/[A-Za-z0-9_]+"
        return bool(re.fullmatch(pattern, param))
    
    def encrypt(self, s: str) -> str:
        result = list()
        string = ""
        previous = ""

        for i in s:
            if previous == "":
                previous = i
                string += i
                continue
            

            if previous == i:
                string += i
            else:
                result.append(string)
                string = i
            previous = i
        result.append(string)

        finall_result = ""
        for i in result:
            encrypted = ""
            for index, char in enumerate(i):
                encrypted += str((ord(char) - 96) * (index + 1))
            finall_result += encrypted
        
        return finall_result