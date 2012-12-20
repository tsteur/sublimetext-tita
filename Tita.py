import sublime, sublime_plugin
import desktop
import os


class BaseCommand(sublime_plugin.WindowCommand):
    def root(self):
        return self.window.folders()[0]

    def settings(self):
        return sublime.load_settings('Tita.sublime-settings')

    def exec_command(self, cmd):
        command = {'cmd': cmd, 'shell': True, 'working_dir': self.root()}
        exec_args = self.settings().get('exec_args')
        exec_args.update(command)
        self.window.run_command("exec", exec_args)


class Titaclean(BaseCommand):

    def run(self, *args, **kwargs):
        sublime.status_message('Clean build directories')
        exec_command(u"titanium clean", self.root(), self.window)


class Titagenerate(BaseCommand):

    def on_done(self, text):
        sublime.status_message('Generate' + text)
        self.exec_command(u"alloy generate " + text)

    def run(self, *args, **kwargs):
        self.window.show_input_panel("alloy generate ", "", self.on_done, None, None)


class TitaCommand(BaseCommand):

    def compilealloy(self, device):
        self.exec_command(u"alloy compile -n --config platform=" + device)
        self.exec_command(u"titanium build --platform=" + device)

    def runalloy(self, device):
        loglevel = self.settings().get('alloy').get('logLevel')
        cmd = u"alloy run -n -l %s %s %s " % (loglevel, self.root(), device)
        self.exec_command(cmd)

    def build(self, device):
        cmd = u"titanium build -p ios -F %s -T simulator --project-dir %s" % (device, self.root())
        self.exec_command(cmd)

    def run(self, device='iphone', *args, **kwargs):
        if ('mobileweb' == device):
            sublime.status_message('Compiling MobileWeb')
            self.compilealloy(device)
            desktop.open('http://127.0.0.1:8020/index.html')
        else:
            self.compilealloy(device);
            sublime.status_message('Running ' + device)
            self.build(device)
