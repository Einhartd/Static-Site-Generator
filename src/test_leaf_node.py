import unittest

from .leaf_node import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_with_prop_html(self):
        node = LeafNode("a", "Whazzup", {"a": "b", "c": "d"})
        self.assertEqual(node.to_html(), '<a a="b" c="d">Whazzup</a>')





    