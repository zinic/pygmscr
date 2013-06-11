import curses
from . import directives


class ComponentMessage(object):

    def __init__(self, directive, payload=None):
        self.directive = directive
        self.payload = payload


class CursesComponent(object):

    def on_input(self, char):
        raise NotImplementedError

    def refresh(self, screen):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


class ScreenDriver(object):

    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        self.screen.keypad(1)

    def destroy(self):
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()

    def run(self, parent_component):
        should_run = True
        while should_run:
            message = parent_component.on_input(self.screen.getch())

            if message:
                if message.directive == directives.EXIT:
                    should_run = False
                    break
                elif message.directive == directives.CLEAR:
                    self.screen.erase()
            self.screen.erase()
            parent_component.refresh(self.screen)
