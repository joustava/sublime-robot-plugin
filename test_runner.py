import sublime
import sublime_plugin

import os
import unittest
import StringIO

plugin_dir = os.getcwd()
test_suites = {
        'tests': ['test.test_get_keyword_at_pos']
}

class RobotPluginRunTestsCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return plugin_dir == os.path.join(sublime.packages_path(), 'Robot Framework')

    def run(self, suite_name):
        print "run invoked"
        bucket = StringIO.StringIO()
        suite = test_suites[suite_name]
        suite = unittest.defaultTestLoader.loadTestsFromName('tests')
        print suite
        unittest.TextTestRunner(stream=bucket, verbosity=1).run(suite)

        print_to_view(self.window.new_file(), bucket.getvalue)


def print_to_view(view, obtain_content):
    edit = view.begin_edit()
    view.insert(edit, 0, obtain_content())
    view.end_edit(edit)
    view.set_scratch(True)

    return view