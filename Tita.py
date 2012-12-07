import sublime, sublime_plugin
import desktop
import os


def settings():
    return sublime.load_settings('Tita.sublime-settings')


class Titagenerate(sublime_plugin.WindowCommand):

    def root(self):
        return self.window.folders()[0]

    def on_done(self, text):
        sublime.status_message('Generate' + text)
        command = {'cmd': u"alloy generate " + text, 
                   'shell': True,
                   'working_dir': self.root()}
        exec_args = settings().get('exec_args')
        exec_args.update(command)
        self.window.run_command("exec", exec_args)

    def run(self, *args, **kwargs):
        self.window.show_input_panel("alloy generate ", "", self.on_done, None, None)


class TitaCommand(sublime_plugin.WindowCommand):

    def root(self):
        return self.window.folders()[0]

    def compilealloy(self, device):
        command = {'cmd': u"alloy compile -n --config platform=" + device, 
                   'shell': True,
                   'working_dir': self.root()}
        exec_args = settings().get('exec_args')
        exec_args.update(command)
        self.window.run_command("exec", exec_args)


    def runalloy(self, device):
        command = {'cmd': u"alloy run -n " + self.root() + ' ' + device, 
                   'shell': True,
                   'working_dir': self.root()}
        exec_args = settings().get('exec_args')
        exec_args.update(command)
        self.window.run_command("exec", exec_args)


    def run(self, device='iphone', *args, **kwargs):
        if ('mobileweb' == device):
            sublime.status_message('Compiling MobileWeb')
            self.compilealloy(device)
            desktop.open(os.path.join(self.root(), 'build', 'mobileweb', 'index.html'))
        else:
            sublime.status_message('Running ' + device)
            self.runalloy(device)
