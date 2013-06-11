import pynsive

import pygmscr.ncurses as ncurses
import pygmscr.terminal as terminal


_TAPP = terminal.TerminalApp

def terminal_app_filter(_class):
    return issubclass(_class, _TAPP)


def load_stock(terminal):
    modules = pynsive.discover_classes('pygmscr.stock')
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
