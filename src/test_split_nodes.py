import unittest

from .text_node import TextType, TextNode
from .split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitNodeDelimiter(unittest.TestCase):
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
        
    def test_multiple_text_with_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        other_node = TextNode("That was text with a `mega code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, other_node], "`", TextType.CODE)
        self.assertEqual(new_nodes,
                            [
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                            TextNode("That was text with a ", TextType.TEXT),
                            TextNode("mega code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                            ])
        
        
class TestSplitNodeImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_no_images(self):
        node = TextNode(
            "This is text without image",
            TextType.TEXT,
        )
        bold_node = TextNode(
            "Me too!",
            TextType.BOLD
        )
        new_nodes = split_nodes_image([node, bold_node])
        self.assertListEqual(
            [
                TextNode("This is text without image",TextType.TEXT),
                TextNode("Me too!",TextType.BOLD)
            ],
            new_nodes
        )
        
    def test_only_image(self):
        node = TextNode(
            "![only images](https://onlyimages.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "only images", TextType.IMAGE, "https://onlyimages.com"
                )
            ],
            new_nodes
        )
        
class TestSplitNodeLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_no_links(self):
        node = TextNode(
            "This is text without link",
            TextType.TEXT,
        )
        bold_node = TextNode(
            "Me too!",
            TextType.BOLD
        )
        new_nodes = split_nodes_link([node, bold_node])
        self.assertListEqual(
            [
                TextNode("This is text without link",TextType.TEXT),
                TextNode("Me too!",TextType.BOLD)
            ],
            new_nodes
        )
        
    def test_only_link(self):
        node = TextNode(
            "[only links](https://onlylinks.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "only links", TextType.LINK, "https://onlylinks.com"
                )
            ],
            new_nodes
        )
        
    def test_with_image(self):
        link_node = TextNode(
            "I am with link [just link](https://link.com)",
            TextType.ITALIC,
        )
        image_node = TextNode(
            "But I am with image ![image](https://image.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([link_node, image_node])
        self.assertListEqual(
            [
                TextNode(
                    "I am with link ", TextType.ITALIC
                ),
                TextNode("just link", TextType.LINK, "https://link.com"),
                TextNode("But I am with image ![image](https://image.com)",
                         TextType.TEXT),
            ],
            new_nodes
        )