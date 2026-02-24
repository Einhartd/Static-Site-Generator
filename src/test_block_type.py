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