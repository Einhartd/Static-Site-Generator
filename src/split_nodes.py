from text_node import TextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes: list[TextNode] = []

    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
        else:
            if old.text.count(delimiter) % 2 != 0:
                raise Exception("Invalid Markdown syntax (err 0)")
            
            split_node = []
            split_node = old.text.split(delimiter)

            if len(split_node) != 3:
                raise Exception("Invalid Markdown syntax (err 1)")
            
            for i in range(len(split_node)):
                if i == 1:
                    split_node[i] = TextNode(split_node[i], text_type=text_type)
                else:
                    split_node[i] = TextNode(split_node[i], TextType.TEXT)

            new_nodes.extend(split_node)

    return new_nodes
    