class NewDict(dict):
    def get(self, key, default_value=0):
        if key in self.keys():
            return self[key]
        else:
            return default_value


new_dict = NewDict({'Васька': 35, 'Женька': 45, 'Вовка': 60})
print(f"Васька: {new_dict.get('Васька')}")
print(f"Ванька : {new_dict.get('Ванька')}")

