from .split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from .text_node import TextNode, TextType

def text_to_textnodes(text:str):
    text_node: list[TextNode] = [TextNode(text=text, text_type=TextType.TEXT)]
    text_bold_node: list[TextNode] = split_nodes_delimiter(text_node, "**", TextType.BOLD)
    text_italic_node: list[TextNode] = split_nodes_delimiter(text_bold_node, "_", TextType.ITALIC)
    text_code_node: list[TextNode] = split_nodes_delimiter(text_italic_node, "`", TextType.CODE)
    text_image_node: list[TextNode] = split_nodes_image(text_code_node)
    text_link_node: list[TextNode] = split_nodes_link(text_image_node)
    return text_link_node
