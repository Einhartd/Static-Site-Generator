import unittest

from text_node import TextType, TextNode
from split_nodes import split_nodes_delimiter

class TestSplitNodeMethod(unittest.TestCase):
    def test_text_with_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,
                         [
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                            ])
        
    def test_start_with_italic(self):
        node = TextNode("_This italic text_ is a test.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
                         [
                             TextNode("", TextType.TEXT),
                             TextNode("This italic text", TextType.ITALIC),
                             TextNode(" is a test.", TextType.TEXT)
                         ])
        
    def test_not_text(self):
        node = TextNode("_Just_ italics_ with error.", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_skip_text(self):
        node_italics = TextNode("I have created ", TextType.ITALIC)
        node = TextNode(" a text _with italics_.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node_italics, node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
                         [
                             TextNode("I have created ", TextType.ITALIC),
                             TextNode(" a text ", TextType.TEXT),
                             TextNode("with italics", TextType.ITALIC),
                             TextNode(".", TextType.TEXT)
                         ])