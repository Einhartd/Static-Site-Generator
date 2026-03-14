import unittest

from .block_type import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_headings(self):
        headings = ["# a", "## b", "### c", "#### d", "##### e", "###### f"]
        test_blocks = []
        for head in headings:
            test_blocks.append(block_to_block_type(head))

        for i in test_blocks:
            self.assertTrue(i, BlockType.HEADING)

    def test_multiline_code(self):
        code = "```\nabcd\n```"
        test_res = block_to_block_type(code)
        self.assertTrue(test_res, BlockType.CODE)

    def test_heading_block(self):
        self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Hello"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Hello"), BlockType.HEADING)

    def test_not_heading_block(self):
        self.assertEqual(block_to_block_type("#Hello"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("####### Hello"), BlockType.PARAGRAPH)

    def test_quote_block(self):
        self.assertEqual(
            block_to_block_type("> line one\n> line two"),
            BlockType.QUOTE,
        )

    def test_invalid_quote_block(self):
        self.assertEqual(
            block_to_block_type("> line one\nline two"),
            BlockType.PARAGRAPH,
        )

    def test_unordered_list_block(self):
        self.assertEqual(
            block_to_block_type("- one\n- two\n- three"),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list_block(self):
        self.assertEqual(
            block_to_block_type("1. one\n2. two\n3. three"),
            BlockType.ORDERED_LIST,
        )

    def test_invalid_ordered_list_block(self):
        self.assertEqual(
            block_to_block_type("1. one\n3. two"),
            BlockType.PARAGRAPH,
        )

    def test_invalid_ordered_list_block_out_of_order(self):
        self.assertEqual(
            block_to_block_type("2. one\n3. two"),
            BlockType.PARAGRAPH,
        )

    def test_code_block(self):
        self.assertEqual(
            block_to_block_type("```\ncode here\n```"),
            BlockType.CODE,
        )