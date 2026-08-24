class ExceptionProxy(Exception):
    def __init__(self, message, functiontion):
        self.message = message
        self.function = functiontion


def transform_exceptions(func_ls: list) -> list[ExceptionProxy]:
    my_list = list()
    for item in func_ls:
        try:
            item()
            Proxy = ExceptionProxy("ok!", item)
            my_list.append(Proxy)
        except Exception as e:
            e = str(e)
            Proxy = ExceptionProxy(e, item)
            my_list.append(Proxy)
    return my_list


