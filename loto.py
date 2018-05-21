#!/usr/bin/python3
from random import randint


def generate_unique_numbers(count, minbound, maxbound):
    if count > maxbound - minbound + 1:
        raise ValueError('Incorrect input parameters')
    ret = []
    while len(ret) < count:
        new = randint(minbound, maxbound)
        if new not in ret:
            ret.append(new)
    return ret


class Keg:
    __num = None

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)


class Card:
    __rows = 3
    __cols = 9
    __nums_in_row = 5
    __data = None
    __emptynum = 0
    __crossednum = -1

    def __init__(self):
        uniques_count = self.__nums_in_row * self.__rows
        uniques = generate_unique_numbers(uniques_count, 1, 90)

        self.__data = []
        for i in range(0, self.__rows):
            tmp = sorted(uniques[self.__nums_in_row * i: self.__nums_in_row * (i + 1)])
            empty_nums_count = self.__cols - self.__nums_in_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self.__emptynum)
            self.__data += tmp

    def __str__(self):
        delimiter = '--------------------------'
        ret = delimiter + '\n'
        for index, num in enumerate(self.__data):
            if num == self.__emptynum:
                ret += '  '
            elif num == self.__crossednum:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.__cols == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__crossednum
                return
        raise ValueError(f'Number not in card: {num}')

    def closed(self) -> bool:
        return set(self.__data) == {self.__emptynum, self.__crossednum}


class Game:
    __usercard = None
    __compcard = None
    __numkegs = 90
    __kegs = []
    __gameover = False

    def __init__(self):
        self.__usercard = Card()
        self.__compcard = Card()
        self.__kegs = generate_unique_numbers(self.__numkegs, 1, 90)

    def play_round(self) -> int:
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - computer wins
        """

        keg = self.__kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'----- Ваша карточка ------\n{self.__usercard}')
        print(f'-- Карточка компьютера ---\n{self.__compcard}')

        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if useranswer == 'y' and not keg in self.__usercard or \
           useranswer != 'y' and keg in self.__usercard:
            return 2

        if keg in self.__usercard:
            self.__usercard.cross_num(keg)
            if self.__usercard.closed():
                return 1
        if keg in self.__compcard:
            self.__compcard.cross_num(keg)
            if self.__compcard.closed():
                return 2

        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('You win')
            break
        elif score == 2:
            print('You lose')
            break
