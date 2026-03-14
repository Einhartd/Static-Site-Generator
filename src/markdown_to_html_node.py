from .html_node import HTMLNode
from .markdown_to_blocks import markdown_to_blocks
from .block_type import BlockType, block_to_block_type
from .parent_node import ParentNode
from .text_node import TextType, TextNode
from .split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from .text_to_html import text_node_to_html_node
from .leaf_node import LeafNode
import re

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks: list[str] = markdown_to_blocks(markdown)
    children: list[HTMLNode] = []

    for block in blocks:
        children.append(block_to_html_node(block))

    return ParentNode("div", children)

def block_to_html_node(block: str) -> HTMLNode:
    block_type: BlockType = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        lines = block.split("\n")
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        text = " ".join(lines)    
        children = text_to_children(text)
        return ParentNode("p", children)
    elif block_type == BlockType.HEADING:
        level = get_heading_level(block)
        if 1 <= level <= 6 and block[level] == " ":
            text = block[level+1:]
            children = text_to_children(text)
            return ParentNode(f"h{level}", children)
        else:
            children = text_to_children(block)
            return ParentNode("p", children)
    elif block_type == BlockType.CODE:
        return ParentNode("pre", [code_block_to_code_node(block)])
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        li_childs = []
        for i in range(len(lines)):
            lines[i] = lines[i][2:]
            ul_child = text_to_children(lines[i])
            li_childs.append(ParentNode("li", ul_child))
        return ParentNode("ul", li_childs)
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        for i in range(len(lines)):
            lines[i] = lines[i][2:].strip()
        text = " ".join(lines)
        children = text_to_children(text)
        return ParentNode("blockquote", children)
    elif block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        ol_children = []
        for i in range(len(lines)):
            lines[i] = re.sub("^(\d+)\.", "", lines[i]).strip()
            item_children = text_to_children(lines[i])
            ol_children.append(ParentNode("li", item_children))
        return ParentNode("ol", ol_children)
        
    raise Exception("unsupported block type")




def code_block_to_code_node(block):
    code_text = block.lstrip('```')
    code_text = code_text.rstrip('```')
    code_text = code_text.lstrip('\n')
    text_node = TextNode(code_text, TextType.TEXT)
    code_html_node = text_node_to_html_node(text_node)
    return ParentNode("code", [code_html_node])

def get_heading_level(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    return level

def text_to_children(text: str) -> list[LeafNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return [text_node_to_html_node(text_node) for text_node in nodes]