import pygmscr.ncurses as ncurses


class TerminalApp(object):

    def name(self):
        raise NotImplementedError

    def desc(self):
        raise NotImplementedError

    def run(self, terminal, args):
        raise NotImplementedError


class Terminal(ncurses.CursesComponent):

    def __init__(self):
        self.current_input = ''
        self.screen_output = list()
        self.applications = list()

    def register_app(self, app):
        self.applications.append(app)

    def collect_input(self, char):
        self.current_input += char

    def find_app(self, name):
        for app in self.applications:
            if app.name() == name:
                return app
        return None

    def refresh(self, screen):
        line = 0
        for output in self.screen_output:
            screen.addstr(line, 0, output)
            line += 1
        screen.addstr(line, 0, self.current_input)
        screen.refresh()

    def process_directive(self, directive):
        if directive == ncurses.CLEAR:
            self.screen_output = list()

    def user_command(self, command):
        self.screen_output.append(command)
        split_cmd = command.split(' ')
        application = self.find_app(split_cmd[0])

        if application:
            result = self.run_app(application, split_cmd[1:])
            if result:
                self.process_directive(result.directive)
                return result
        else:
            self.screen_output.append(
                'No program named, "{}" is available.'.format(split_cmd[0]))

    def run_app(self, application, args):
        result = application.run(self, args)
        if result:
            return self.handle_result(type(result), result)

    def handle_result(self, result_type, result):
        if result_type is str:
            for line in result.split('\n'):
                self.screen_output.append(line)
        elif result_type is ncurses.ComponentMessage:
            return result

    def on_input(self, char):
        #self.screen_output.append(str(char))

        if char == 4:
            return ncurses.ComponentMessage(ncurses.EXIT)
        if char == 263:
            input_len = len(self.current_input)
            if input_len > 0:
                self.current_input = self.current_input[:input_len-1]
            return ncurses.ComponentMessage(ncurses.CLEAR)
        if char == ord('\n'):
            command = self.current_input
            self.current_input = ''
            return self.user_command(command)
        elif char > 31 and char < 127:
            self.collect_input(chr(char))
