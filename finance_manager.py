#Импортируем класс
from finance_record import FinanceRecord

class FinanceManager:
    def __init__(self, filename):
        self.filename = filename

    def add_record(self, record):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(str(record.to_dict()) + '\n')

    def edit_record(self, index, new_record):
        records = self.read_records()
        if 0 <= index < len(records):
            records[index] = new_record
            self.save_records(records)

    def delete_record(self, index):
        records = self.read_records()
        if 0 <= index < len(records):
            del records[index]
            self.save_records(records)

    def search_records(self, keyword):
        records = self.read_records()
        return [record for record in records if keyword.lower() in str(record).lower()]

    def read_records(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [FinanceRecord.from_dict(eval(line.strip())) for line in lines]

    def save_records(self, records):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for record in records:
                file.write(str(record.to_dict()) + '\n')
