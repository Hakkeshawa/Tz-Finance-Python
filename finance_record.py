#Описание 
class FinanceRecord:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"Дата: {self.date}\nКатегория: {self.category}\nСумма: {self.amount}\nОписание: {self.description}"

    def to_dict(self):
        return {
            'date': self.date,
            'category': self.category,
            'amount': self.amount,
            'description': self.description
        }

    @staticmethod
    def from_dict(record_dict):
        return FinanceRecord(record_dict['date'], record_dict['category'], record_dict['amount'], record_dict['description'])
