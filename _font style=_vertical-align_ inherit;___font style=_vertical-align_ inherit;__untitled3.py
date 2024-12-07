class Employee:
    def __init__(self, name, position, salary):
        """
        Ініціалізує об'єкт працівника.
        :param name: Ім'я працівника
        :param position: Посада працівника
        :param salary: Заробітна плата працівника
        """
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        """
        Повертає рядок з інформацією про заробітну плату.
        :return: Рядок у форматі "Заробітна плата [ім'я]: [заробітна плата]"
        """
        return f"Заробітна плата {self.name}: {self.salary} грн"


# Приклад використання
if __name__ == "__main__":
    # Створення об'єкта працівника
    employee = Employee("Олена", "Менеджер", 15000)

    # Виведення інформації про заробітну плату
    print(employee.get_salary_info())  # Виведе: "Заробітна плата Олена: 15000 грн"
