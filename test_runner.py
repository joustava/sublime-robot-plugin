import os, sys
lib_path = os.path.normpath(os.path.join(os.getcwd(), 'lib/'))
if lib_path not in sys.path:
    sys.path.append(lib_path)
pyd_path = os.path.dirname(sys.executable)
if pyd_path not in sys.path:
    sys.path.append(pyd_path)


import os
import unittest
import StringIO



plugin_dir = os.getcwd()
test_suites = {
        'tests': ['tests.test_get_keyword_at_pos'],
        'example': ['tests.test_sequence_functions']
}




def run_tests():
    print "run invoked"
    bucket = StringIO.StringIO()
    suite = test_suites['tests']
    suite = unittest.defaultTestLoader.loadTestsFromName(suite[0])
    unittest.TextTestRunner(verbosity=9).run(suite)


run_tests()