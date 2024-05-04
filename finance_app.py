# Импортируем классы со сторонних файлов
from finance_manager import FinanceManager
from finance_record import FinanceRecord

#Само по себе приложение
class FinancialApp:
    def __init__(self, filename):
        self.manager = FinanceManager(filename)

#Пока программа запущена - выводим выбор действия
    def run(self):
        while True:
            print("\nВыберите действие:")
            print("1. Показать баланс")
            print("2. Добавить запись")
            print("3. Редактировать запись")
            print("4. Удалить запись")
            print("5. Поиск записей")
            print("6. Выйти")

            choice = input("Введите номер действия: ")

#Вызываем функции когда выбираем нужное нам действие
            if choice == '1':
                self.show_balance()
            elif choice == '2':
                self.add_record()
            elif choice == '3':
                self.edit_record()
            elif choice == '4':
                self.delete_record()
            elif choice == '5':
                self.search_records()
            elif choice == '6':
                print("До свидания!")
                break
            else:
                print("Неверный ввод. Пожалуйста, введите число от 1 до 6.")

#Сама работа функций
    def show_balance(self):
        records = self.manager.read_records()
        incomes = sum(record.amount for record in records if record.category == 'Доход')
        expenses = sum(record.amount for record in records if record.category == 'Расход')
        balance = incomes - expenses
        print(f"\nТекущий баланс: {balance}")
        print(f"Доходы: {incomes}")
        print(f"Расходы: {expenses}")

    def add_record(self):
        date = input("Введите дату записи (гггг-мм-дд): ")
        category = input("Введите категорию (Доход/Расход): ")
        amount = float(input("Введите сумму: "))
        description = input("Введите описание: ")
        record = FinanceRecord(date, category, amount, description)
        self.manager.add_record(record)
        print("Запись добавлена успешно.")

    def edit_record(self):
        index = int(input("Введите номер записи для редактирования: "))
        records = self.manager.read_records()
        if 0 <= index < len(records):
            date = input("Введите новую дату записи (гггг-мм-дд): ")
            category = input("Введите новую категорию (Доход/Расход): ")
            amount = float(input("Введите новую сумму: "))
            description = input("Введите новое описание: ")
            new_record = FinanceRecord(date, category, amount, description)
            self.manager.edit_record(index, new_record)
            print("Запись успешно отредактирована.")
        else:
            print("Неверный номер записи.")

    def delete_record(self):
        index = int(input("Введите номер записи для удаления: "))
        self.manager.delete_record(index)
        print("Запись успешно удалена.")

    def search_records(self):
        keyword = input("Введите ключевое слово для поиска: ")
        found_records = self.manager.search_records(keyword)
        if found_records:
            print("\nНайденные записи:")
            for record in found_records:
                print(record)
        else:
            print("Записи не найдены.")
