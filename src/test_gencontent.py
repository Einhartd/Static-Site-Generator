import unittest
from .gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        title = extract_title(markdown)
        self.assertEqual(title, "Hello")

    def test_extract_title_no_h1(self):
        markdown = "## Not a title"
        with self.assertRaises(Exception):
            extract_title(markdown)