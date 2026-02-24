import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"

def block_to_block_type(text_block):
    heading_regex: str = r"^#{1,6}\s.*"
    multiline_code_regex: str = r"(`{3})\n(.*)\n(`{3})"
    quote_regex: str = r">(\s*).+"
    unordered_regex: str = r"-\s(.*)"
    ordered_regex: str = r"\d.\s"

    block_regex: list[tuple] = [(heading_regex, BlockType.HEADING),
                                (multiline_code_regex, BlockType.CODE), 
                                (quote_regex, BlockType.QUOTE),
                                (unordered_regex, BlockType.UNORDERED_LIST),
                                (ordered_regex, BlockType.ORDERED_LIST)
                                ]

    for reg, block_type in block_regex:
        found_regex = re.findall(reg, text_block)
        if found_regex:
            if block_type == BlockType.ORDERED_LIST:
                for i, val in enumerate(found_regex):
                    found_regex[i] = int(found_regex[i][0])
                res = found_regex == sorted(found_regex) and len(set(found_regex)) == len(found_regex)
                if res:
                    return block_type
            else:
                return block_type

    return BlockType.PARAGRAPH