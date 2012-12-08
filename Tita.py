import sublime, sublime_plugin
import desktop
import os


def settings():
    return sublime.load_settings('Tita.sublime-settings')


def exec_command(cmd, path, window):
    command = {'cmd': cmd, 'shell': True, 'working_dir': path}
    exec_args = settings().get('exec_args')
    exec_args.update(command)
    window.run_command("exec", exec_args)


class Titaclean(sublime_plugin.WindowCommand):

    def root(self):
        return self.window.folders()[0]

    def run(self, *args, **kwargs):
        sublime.status_message('Clean build directories')
        exec_command(u"titanium clean", self.root(), self.window)


class Titagenerate(sublime_plugin.WindowCommand):

    def root(self):
        return self.window.folders()[0]

    def on_done(self, text):
        sublime.status_message('Generate' + text)
        exec_command(u"alloy generate " + text, self.root(), self.window)

    def run(self, *args, **kwargs):
        self.window.show_input_panel("alloy generate ", "", self.on_done, None, None)


class TitaCommand(sublime_plugin.WindowCommand):

    def root(self):
        return self.window.folders()[0]

    def compilealloy(self, device):
        exec_command(u"alloy compile -n --config platform=" + device, self.root(), self.window)
        exec_command(u"titanium build --platform=" + device, self.root(), self.window)

    def runalloy(self, device):
        exec_command(u"alloy run -n " + self.root() + ' ' + device, self.root(), self.window)

    def run(self, device='iphone', *args, **kwargs):
        if ('mobileweb' == device):
            sublime.status_message('Compiling MobileWeb')
            self.compilealloy(device)
            desktop.open('http://127.0.0.1:8020/index.html')
        else:
            sublime.status_message('Running ' + device)
            self.runalloy(device)
