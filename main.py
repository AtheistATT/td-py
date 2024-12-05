import curses
import time
import logic

main_logic =logic.GameLogic()
def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)

    if curses.has_colors():
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)

    while True:
        key = stdscr.getch()
        stdscr.addstr(0, 0, main_logic.update_game_state())
        if key == curses.KEY_UP:
            stdscr.addstr(0,0, main_logic.update_game_state("KEY_UP"))
            stdscr.clear()
            stdscr.refresh()
            continue
        stdscr.refresh()
        time.sleep(1)
curses.wrapper(main)
