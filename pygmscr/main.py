import pygmscr.ncurses as ncurses
import pygmscr.plugin as plugin
import pygmscr.terminal as terminal

_TERMINAL_APP_CLASS = type(terminal.TerminalApp)

def terminal_app_filter(_class):
    return issubclass(_class, _TERMINAL_APP_CLASS)


def load_stock(terminal):
    mod_inspector = plugin.module_inspector()
    modules = mod_inspector.find_classes_in_module(
        'pygmscr.stock', terminal_app_filter)
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
