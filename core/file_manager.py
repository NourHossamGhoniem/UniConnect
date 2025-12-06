# core/file_manager.py

class FileManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FileManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.storage = {}  # هيكون dictionary بدل CSV فعلي

    def read_csv(self, filename):
        return self.storage.get(filename, [])

    def append_csv(self, filename, data_dict, fieldnames=None):
        if filename not in self.storage:
            self.storage[filename] = []
        self.storage[filename].append(data_dict)

    def write_csv(self, filename, data_list, fieldnames=None):
        self.storage[filename] = data_list
