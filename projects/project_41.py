class Proxy:
    def __init__(self, obj: object) -> None:
        self._obj = obj
        self._last_accessed = None
        self._access_counts = {}

    def last_accessed_attribute(self) -> str:
        if self._last_accessed == None:
            raise Exception("No attribute was accessed.")
        return self._last_accessed

    def count_of_accesses(self, attribute_name: str) -> int:
        if attribute_name not in self._access_counts:
            return 0
        else:
            return self._access_counts[attribute_name]
            
    def was_accessed(self, attribute_name: str) -> bool:
        if attribute_name not in self._access_counts:
            return False
        else:
            return True

    def __getattr__(self, name):
        if not hasattr(self._obj, name):
            raise Exception("No such attribute.")     
         
        self._last_accessed = name

        if name not in self._access_counts:      
            self._access_counts[name] = 1
        else:
            self._access_counts[name] += 1

        return getattr(self._obj, name)