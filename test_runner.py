import os, sys, re
lib_path = os.path.normpath(os.path.join(os.getcwd(), 'lib/'))
if lib_path not in sys.path:
    sys.path.append(lib_path)
pyd_path = os.path.dirname(sys.executable)
if pyd_path not in sys.path:
    sys.path.append(pyd_path)

import unittest
import StringIO

from robot import run

reloading = {
    'happening': False,
    'shown': False
}

#Sublime does not auto reload submodules. Which would be very awesome while developing a plugin.
def reload_modules():
    reload_mods = []
    for mod in sys.modules:
        if (mod[0:13] == 'robot_plugin.' or mod == 'robot_plugin') and sys.modules[mod] != None:
            reload_mods.append(mod)
            reloading['happening'] = True

    #These must be in this particular order
    mods_load_order = [
        'robot_plugin',
        'robot_plugin.tests',
        'robot_plugin.tests.test_get_keyword_at_pos',
        'robot_plugin.tests.test_sequence_functions',
        'robot_plugin.helpers'
    ]

    for mod in mods_load_order:
        if mod in reload_mods:
            reload(sys.modules[mod])


plugin_dir = os.getcwd()
test_suites = {
        'tests': ['robot_plugin.tests.test_get_keyword_at_pos']
}

def run_unittests():
    reload_modules()
    print "RUNNING TESTS"
    io = StringIO.StringIO()
    suite = test_suites['tests']
    suite = unittest.defaultTestLoader.loadTestsFromName(suite[0])
    unittest.TextTestRunner(verbosity=9).run(suite)

def run_acceptance_tests():
    reload_modules()
    io = StringIO.StringIO()
    run.run('lib/robot_plugin/tests/example_test.py', stdout=io)


reload_modules()
run_unittests()
run_acceptance_tests()

