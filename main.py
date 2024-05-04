# Инициализируем запуск программы
if __name__ == "__main__":
    from finance_app import FinancialApp

    filename = "finance_records.txt"
    app = FinancialApp(filename)
    app.run()
