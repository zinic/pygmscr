import random
import pygmscr.terminal as terminal


class EclipsePhaseRoll(terminal.TerminalApp):

    def __init__(self):
        pass

    def name(self):
        return 'ec_roll'

    def desc(self):
        return 'Makes an Eclipse Phase dice roll'

    def run(self, terminal, args):
        tens = self.roll(10)
        ones = self.roll(10)
        if tens == 0:
            return '{}'.format(ones)
        else:
            return '{}{}'.format(tens, ones)

    def roll(self, sides):
        return int(random.random() * sides)
