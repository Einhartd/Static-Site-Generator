import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_child_eq(self):
        node_child = HTMLNode("h1", "test_eq")
        node = HTMLNode("p", "main_node", [node_child], {"href": "https://www.google.com"})
        print(node)
        self.assertEqual(node.children[0], node_child)

    def test_none_eq(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        test_prop = {"href": "https://www.google.com",
                     "target": "_blank",}
        node = HTMLNode(props=test_prop)
        expected_result = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)
    