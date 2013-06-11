import pynsive

import pygmscr.ncurses as ncurses
import pygmscr.terminal as terminal


def terminal_app_filter(_class):
    return issubclass(_class, terminal.TerminalApp)


def load_stock(terminal):
    modules = pynsive.list_classes('pygmscr.stock', terminal_app_filter)
    print('Num modules {} - {}'.format(len(modules), modules))
    for _class in modules:
        terminal.register_app(_class())


if __name__ == '__main__':
    terminal = terminal.Terminal()
    load_stock(terminal)

    try:
        screen_driver = ncurses.ScreenDriver()
        screen_driver.run(terminal)
    finally:
        screen_driver.destroy()
