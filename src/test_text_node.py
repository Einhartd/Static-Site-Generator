import unittest

from text_node import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_bold_italic(self):
        node_italic = TextNode("This text is italic", TextType.ITALIC)
        node_bold = TextNode("This text is bold", TextType.BOLD)
        self.assertNotEqual(node_italic, node_bold)

    def test_empty_url(self):
        empty_url_node = TextNode("Empty url text", TextType.LINK)
        self.assertEqual(empty_url_node.url, None)

    def test_url_filled(self):
        url_node = TextNode("Filled url text", TextType.LINK, url = "test1")
        self.assertEqual(url_node.url, "test1")


if __name__ == "__main__":
    unittest.main()
