"""Модуль приложения"""


class ListComparator:
    """
    Класс для сравнения списков чисел и расчета их средних значений
    """
    @staticmethod
    def calculate_average(lst):
        """
        Рассчитывает среднее значение списка.
        """
        return sum(lst) / len(lst) if lst else 0

    def compare_lists(self, list1, list2):
        """
        Сравнивает средние значения двух списков и возвращает соответствующее сообщение.
        """
        avg1 = self.calculate_average(list1)
        avg2 = self.calculate_average(list2)
        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
