import random
import pygmscr.terminal as terminal


class Roll(terminal.TerminalApp):

    def __init__(self):
        pass

    def name(self):
        return 'roll'

    def desc(self):
        return """Makes a dice roll formatted with xds + c where x is the number of
dice and s is the number of sides on the dice.
"""

    def run(self, terminal, args):
        if len(args) == 0:
            return self.desc()
        else:
            return self.parse_roll(args[0])

    def roll(self, sides):
        return 1 + int(random.random() * sides)

    def parse_roll(self, expression):
        output = ''
        number = 0
        total = 0
        num_die = 1
        reading_sides = False

        for char in expression:
            char_code = ord(char)

            if char_code > 47 and char_code < 58:
                number *= 10
                number += char_code - 48

            if char == 'd':
                reading_sides = True
                num_die = number
                number = 0

        while num_die > 0:
            num_die -= 1
            roll = self.roll(number)
            total += roll
            output += '[{}]'.format(roll)
            output += ',' if num_die > 0 else ' '

        output += '- Total: {}'.format(total)
        return output



