import csv, os
from typing import List, Dict, Optional

class FileManager:
    def read_csv(self, filename: str) -> Optional[List[Dict[str,str]]]:
        if not os.path.exists(filename):
            return []
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    def append_csv(self, filename: str, data_dict: Dict[str,str], fieldnames: List[str]):
        exists = os.path.exists(filename)
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not exists:
                writer.writeheader()
            writer.writerow({k: data_dict.get(k, "") for k in fieldnames})
