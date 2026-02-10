import unittest

from parent_node import ParentNode
from leaf_node import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(tag=None, children=[child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_children_and_prop(self):
        child_node = LeafNode("span", "child", props={"a": "b", "c": "d"})
        parent_node = ParentNode("div", [child_node], props={"e": "f", "g": "h"})
        self.assertEqual(
            parent_node.to_html(),
            f'<div e="f" g="h"><span a="b" c="d">child</span></div>'
        )


