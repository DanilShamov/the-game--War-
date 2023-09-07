# Игры
# Демонстрирует создание модуля
class Player(object):
    """ Участник игры"""
    def __init__ (self, name, score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
def ask_yes_no(question):
        """Задаёт вопрос с ответом 'да' или 'нет'."""
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response
def ask_number(question, low, high):
        """Просит ввести число из заданного диапозона."""
        response = None
        while response not in range(low, high):
            try:
                response = int(input(question))
            except ValueError:
                print("Это не число!")

        return response
if __name__ == "__main__":
    print("Вы запустили модуль напрямую, а не импортировали его.")
    input("\n\n Нажмите Enter, что бы выйти.")
