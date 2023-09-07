# Однокарточная версия игры война
# Псевдокод
# 1 запрашивает количество игроков и их имена
# Раздаёт каждому игроку по 1 карте из колоды
# Показывает номинал вместе с именем игрока
# Выйгрывает игрок с большим номиналом, туз считается за 11 очков
import games, cards

#Создаём новый класс
# Добовляем метод value для определения стоимости карты в руке
# Создаём атрибут ценности туза равной 11
class DeckWar(cards.Deck):
    def populate(self):
        for suit in CardWar.SUITS:
            for rank in CardWar.RANKS:
                self.add(CardWar(rank, suit))

class CardWar(cards.Card):
    """Игрок"""
    @property
    def value(self):
        """Определяем значимость карт"""
        v = self.RANKS.index(self.rank) + 1
        if v > 10:
            v = 10
        if v == 1:
            v = 11
        return v
class Player(cards.Hand):
    def __init__(self, name):
        """Добовляем классу атрибут имени"""
        super(Player, self).__init__()
        self.name = name
class Game():
    def __init__(self):
        """Создаём колоду и список имён и список игроков."""
        self.deck = DeckWar()
        self.names = []
        self.players = []
    def clear_all(self):
        """Удалить все результаты прошлой игры"""
        for player in self.players:
            player.clear()
        self.names = []
        self.players = []
        self.deck.clear()
    def winner(self, players):
        """Определяет победителя."""
        #Список чисел, большее число выйгрывает
        # Нужно выйвить максимальное большие числа и эти игроки победили
        list_numb = []
        winners = []
        for player in players:
            list_numb.append(player.cards[0].value)
        max_numb = max(list_numb)
        for player in players:
            if player.cards[0].value == max_numb:
                winners.append(player)
        return winners
    def play(self):
        """Основной метод для старта игры"""
        self.deck.populate()
        self.deck.shuffle()
        numb = games.ask_number("Сколько игроков будет играть? (1-8)", low = 1, high = 9)
        for bymer in range(numb):
            name = input("Введите ваше имя.")
            self.names.append(name)
        for bymer in self.names:
            self.players.append(Player(bymer))
        self.deck.deal(self.players)
        for player in self.players:
            print(player.name, "имеет карту", player.cards[0], " с ценностью", player.cards[0].value)
        winners = self.winner(self.players)
        print("\n\nНаши победители:")
        for winner in winners:
            print("Победитель", winner.name)
        self.clear_all()

def main():
    game = Game()
    response = None
    while response != "n":
        game.play()
        response = games.ask_yes_no("\nХотите сыграть снова?\n\n")
    input("Нажмите Enter, что бы выйти")

main()
            
