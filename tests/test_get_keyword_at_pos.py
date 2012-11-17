import unittest
from keyword_parse import get_keyword_at_pos

class TestGetKeywordAtPos(unittest.TestCase):
    def test_edges(self):
        self.assertEqual(get_keyword_at_pos('', 0), None)
        self.assertEqual(get_keyword_at_pos('A', 0), 'A')
        self.assertEqual(get_keyword_at_pos('A', 1), 'A')
        for i in range(0, 3):
            self.assertEqual(get_keyword_at_pos('AB', i), 'AB')
        for i in range(0, 4):
            self.assertEqual(get_keyword_at_pos('A B', i), 'A B')
        self.assertEqual(get_keyword_at_pos('   A', 4), 'A')
        self.assertEqual(get_keyword_at_pos('A   ', 0), 'A')

    def test_splitting(self):
        self.assertEqual(get_keyword_at_pos('ABC  DEF', 1), 'ABC')
        self.assertEqual(get_keyword_at_pos('ABC  DEF', 5), 'DEF')
        self.assertEqual(get_keyword_at_pos('ABC  DEF', 6), 'DEF')
        self.assertEqual(get_keyword_at_pos('  ABC  DEF  ', 3), 'ABC')
        self.assertEqual(get_keyword_at_pos('  ABC  DEF  ', 8), 'DEF')

    def test_inbetween_spaces(self):
        self.assertEqual(get_keyword_at_pos('ABC  DEF', 4), None)
        self.assertEqual(get_keyword_at_pos('  ', 0), None)
        self.assertEqual(get_keyword_at_pos('  ', 1), None)
        self.assertEqual(get_keyword_at_pos('  ', 2), None)
        self.assertEqual(get_keyword_at_pos('   A', 0), None)

    def test_samples(self):
        self.assertEqual(get_keyword_at_pos('This Is A Keyword', 3), 'This Is A Keyword')
        self.assertEqual(get_keyword_at_pos('This Is A Keyword', 17), 'This Is A Keyword')
        self.assertEqual(get_keyword_at_pos('Run    Some Keyword', 11), 'Some Keyword')

    def test_tab_char(self):
        self.assertEqual(get_keyword_at_pos('Run\tSome Keyword', 5), 'Some Keyword')

