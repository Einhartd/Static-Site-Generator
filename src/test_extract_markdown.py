import unittest

from .extract_markdown import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is test text with a [nice link](hello!) and [this one](hi!)"
        )
        self.assertListEqual([("nice link", "hello!"), ("this one", "hi!")], matches)
        
    def test_extract_markdown_empty_img(self):
        matches = extract_markdown_images(
            "This is a text without image"
        )
        self.assertListEqual([], matches)
        
    def test_extract_markdown_empty_links(self):
        matches = extract_markdown_links(
            "This is a text without link"
        )
        self.assertListEqual([], matches)
        
    def test_extract_image_but_link(self):
        matches = extract_markdown_images(
            "This is test text with a [nice link](hello!) and [this one](hi!)"
        )
        self.assertListEqual([], matches)
        
    def test_extract_link_but_image(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)  