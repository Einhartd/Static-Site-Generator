import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"

def block_to_block_type(text_block: str) -> BlockType:
    heading_regex: str = r"^#{1,6}\s.*"
    quote_regex: str = r"^>(\s*).*"
    unordered_regex: str = r"^-\s(.*)"
    ordered_regex: str = r"^(\d+)\.\s.+"

    lines = text_block.split("\n")

    if len(lines)==1 and re.findall(heading_regex, lines[0]):
        return BlockType.HEADING
    elif all(re.match(quote_regex, line) for line in lines):
        return BlockType.QUOTE
    elif all(re.match(unordered_regex, line) for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(re.match(ordered_regex, line) for line in lines):
        num_list = []
        for line in lines:
            match = re.match(ordered_regex, line)
            if match:
                num = int(match.group(1))
            else:
                num = 0
            num_list.append(num)
        if num_list[0] == 1 and all(x == y - 1 for x, y in zip(num_list, num_list[1:])):
            return BlockType.ORDERED_LIST
    elif len(lines) >= 2 and lines[0] == "```" and lines[-1] == "```":
        return BlockType.CODE

    return BlockType.PARAGRAPH