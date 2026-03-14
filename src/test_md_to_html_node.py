import unittest
from .markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_single_paragraph_plain_text(self):
        md = """
            hello world
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>hello world</p></div>")

    def test_paragraph_block(self):
        md = """
            This is **bold** text
            and this is still the same paragraph
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bold</b> text and this is still the same paragraph</p></div>",
        )

    def test_heading_h1(self):
        md = """
            # Hello world
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Hello world</h1></div>")

    def test_heading_h3(self):
        md = """
            ### Hello world
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h3>Hello world</h3></div>")

    def test_heading_with_inline_markdown(self):
        md = """
            ## A **bold** heading
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h2>A <b>bold</b> heading</h2></div>")

    def test_headings(self):
        md = """
            # test

            ## test2
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>test</h1><h2>test2</h2></div>",
        )

    def test_invalid_heading_becomes_paragraph(self):
        md = """
            ####### not a heading
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>####### not a heading</p></div>",
        )

    def test_unordered_list(self):
        md = """
            - one
            - two
            - three
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>one</li><li>two</li><li>three</li></ul></div>",
        )

    def test_blockquote(self):
        md = """
            > This is a quote
            > with **bold** text
            > and _italic_ text
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <b>bold</b> text and <i>italic</i> text</blockquote></div>",
        )

    def test_ordered_list(self):
        md = """
            1. First item
            2. Second item with **bold**
            3. Third item with _italic_
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <i>italic</i></li></ol></div>",
        )


    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )