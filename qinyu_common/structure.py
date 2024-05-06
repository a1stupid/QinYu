from qinyu_common.io import save_json, load_json

class Serializable():
    def load_json(self, path):
        item = load_json(path)
        return self.copy_from(item)

    # def copy_from(self, item):
    #     self.__dict__ == item.__dict__

class SerializableDict(Serializable, dict):
    def save_json(self, path):
        save_json(self, path)

    def copy_from(self, item):
        if isinstance(item, dict):
            self.clear()
            self.update(item)
