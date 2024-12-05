import os

class MainScreen:
    screen = []
    hint = ''
    coin = 3
    def __init__(self):
        self.init_screen()

    def init_screen(self):
        self.screen = [['.' for _ in range(30)] for _ in range(10)] 
        self.hint = 'Подсказка\n Стрелки - движение героя'

    def get_screen(self):
        screen_str =''
        for i in range(30):
            for j in range(10):
                screen_str += self.screen[j][i]
            screen_str += '\n'
        screen_str += self.hint + '\n'
        screen_str += 'Монеты:' + str(self.coin)
        return screen_str

    def set_screen(self, x, y, sym):
        self.screen[x][y] = sym
