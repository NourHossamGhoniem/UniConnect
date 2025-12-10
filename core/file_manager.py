import csv
import os

class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data_folder = "data/" 
        return cls._instance

    def read_csv(self, filename):
        path = self.data_folder + filename
        with open(path, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def append_csv(self, filename, data_dict, fieldnames):
        path = self.data_folder + filename
        with open(path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(data_dict)

    def write_csv(self, filename, data_list, fieldnames):
        path = os.path.join(self.data_folder, filename)
        with open(path, mode='w', newline='', encoding='utf-8') as f:
            # We add extrasaction='ignore' so it drops 'members' and works safely
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data_list)