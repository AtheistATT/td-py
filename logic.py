import screen
import random

class GameLogic():
    main_scr = screen.MainScreen()
    fount_col = 1

    def __init__(self):
        pass

    def update_game_state(self, key = ''):
        if key == '':
            self.main_scr.set_screen(0, 0, str(random.randint(0,9)))
        else:
            self.main_scr.set_screen(0,1, 'hi')
        return self.main_scr.get_screen()
