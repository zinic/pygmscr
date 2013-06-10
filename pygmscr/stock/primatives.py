import pygmscr.ncurses as ncurses
import pygmscr.terminal as terminal


class QuitTerminal(terminal.TerminalApp):

    def name(self):
        return 'quit'

    def desc(self):
        return 'exits the gm terminal'

    def run(self, terminal, args):
        return ncurses.ComponentMessage(ncurses.EXIT)


class ClearScreen(terminal.TerminalApp):

    def name(self):
        return 'clear'

    def desc(self):
        return 'Clears the screen'

    def run(self, terminal, args):
        return ncurses.ComponentMessage(ncurses.CLEAR)


class TerminalHelp(terminal.TerminalApp):

    def name(self):
        return 'help'

    def desc(self):
        return """help [command]
Prints a list of available commands or the help information
of the command of the same name as the optionl command
argument.
"""

    def format_application_list(self, applications):
        output = ''
        for app in applications:
            output += '{} - {}\n'.format(app.name(), app.desc())
        return output

    def run(self, terminal, args):
        if len(args) == 0:
            return self.format_application_list(terminal.applications)
        else:
            application = terminal.find_app(args[0])
            if application:
                return application.desc()
            else:
                return 'No program named, "{}" is available.'.format(args[0])
