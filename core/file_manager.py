import csv
import os

class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
        return cls._instance

    def read_csv(self, filename):
        path = f"data/{filename}"
        if not os.path.exists(path):
            return []
        with open(path, mode='r', encoding='utf-8') as file:
            return list(csv.DictReader(file))

    def append_csv(self, filename, data_dict, fieldnames):
        path = f"data/{filename}"
        file_exists = os.path.exists(path)
        with open(path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data_dict)