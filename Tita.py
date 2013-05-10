import sublime, sublime_plugin
import desktop
import os


class TitaAutoClean(sublime_plugin.EventListener):

    def on_post_save(self, view):
        current_file = view.file_name()

        if 'tiapp.xml' in current_file:
            view.window().run_command('titaclean')


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

    def show_quick_panel(self, options, done):
        sublime.set_timeout(lambda: self.window.show_quick_panel(options, done), 10)


class Titaclean(BaseCommand):

    def run(self, *args, **kwargs):
        sublime.status_message('Clean build directories')
        self.exec_command(u"titanium clean")


class Titagenerate(BaseCommand):

    def on_done(self, text):
        sublime.status_message('Generate' + text)
        self.exec_command(u"alloy generate " + text)

    def run(self, *args, **kwargs):
        self.window.show_input_panel("alloy generate ", "", self.on_done, None, None)


class Titalint(BaseCommand):
    osNames = ["android", "iphone", "ipad", "mobileweb"]

    def on_done(self, selectedIndex):
        if selectedIndex < 0:
            return

        osName = self.osNames[selectedIndex]
        sublime.status_message('Run Titanium Code Processor')
        removecolors = "col -b"
        cmd = u"titanium-code-processor analyze --osname %s --all-plugins | %s" % (osName, removecolors)
        self.exec_command(cmd)

    def run(self, *args, **kwargs):
        print "run"
        self.show_quick_panel(self.osNames, self.on_done)


class TitaCommand(BaseCommand):

    def log_level(self):
        return self.settings().get('alloy').get('logLevel')

    def android_sdk_path(self):
        return self.settings().get('android_sdk_path')

    def compile_alloy(self, device):
        self.exec_command(u"alloy compile -n --config platform=" + device)

    def build(self, device, target):
        loglevel = self.log_level()

        if ('iphone' == device or 'ipad' == device):
            cmd = u"titanium build -p ios -F %s -T %s --log-level %s" % (device, target, loglevel)
        if ('android' == device):
            androidsdkpath = self.android_sdk_path()
            cmd = u"titanium build -p %s -T %s -A %s --log-level %s" % (device, target, androidsdkpath, loglevel)
        else:
            cmd = u"titanium build -p %s --log-level %s" % (device, loglevel)

        self.exec_command(cmd)

    def run(self, device='iphone', target='', *args, **kwargs):
        self.compile_alloy(device)
        self.build(device, target)

        if ('mobileweb' == device):
            desktop.open('http://127.0.0.1:8020/index.html')
