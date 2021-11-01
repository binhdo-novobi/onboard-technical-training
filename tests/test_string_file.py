import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sources')))
import io
import unittest
from my_string_file import *


class TestStringFile(unittest.TestCase):
    filein = "text.txt"
    fileout = "out.txt"
    with open(filein, 'r') as fin:
        text = fin.read()
    count_dict = {'lorem': 1, 'ipsum': 1, 'dolor': 2, 'sit': 1, 'amet': 1, 'consectetur': 1, 'adipiscing': 1,
        'elit': 1, 'sed': 1, 'do': 1, 'eiusmod': 1, 'tempor': 1, 'incididunt': 1, 'ut': 3,
        'labore': 1, 'et': 1, 'dolore': 2, 'magna': 1, 'aliqua': 1, 'enim': 1, 'ad': 1, 'minim': 1,
        'veniam': 1, 'quis': 1, 'nostrud': 1, 'exercitation': 1, 'ullamco': 1, 'laboris': 1,
        'nisi': 1, 'aliquip': 1, 'ex': 1, 'ea': 1, 'commodo': 1, 'consequat': 1, 'duis': 1,
        'aute': 1, 'irure': 1, 'in': 3, 'reprehenderit': 1, 'voluptate': 1, 'velit': 1, 'esse': 1,
        'cillum': 1, 'eu': 1, 'fugiat': 1, 'nulla': 1, 'pariatur': 1, 'excepteur': 1, 'sint': 1,
        'occaecat': 1, 'cupidatat': 1, 'non': 1, 'proident': 1, 'sunt': 1, 'culpa': 1, 'qui': 1,
        'officia': 1, 'deserunt': 1, 'mollit': 1, 'anim': 1, 'id': 1, 'est': 1, 'laborum': 1}

    def test_count_words(self):
        self.assertEqual(count_words(self.text), self.count_dict)

    def test_write_file(self):
        write_file(self.count_dict, self.fileout)
        with open(self.fileout, 'r') as f:
            result = f.read()
        expected_output = "dolor,ut,dolore,in"
        self.assertEqual(result, expected_output)

    def test_check_word_exist(self):
        result = check_word_exist(self.count_dict, "in")
        self.assertEqual(result, 3)

    def test_check_word_not_exist(self):
        result = check_word_exist(self.count_dict, "aaa")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringFile)
    unittest.TextTestRunner(verbosity=2).run(suite)
