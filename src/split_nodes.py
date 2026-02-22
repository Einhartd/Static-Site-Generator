from .text_node import TextType, TextNode
from .extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes: list[TextNode] = []
    split_text: list[str] = []
    split_node: list[TextNode] = []

    for old in old_nodes:
        
        split_node.clear()
        
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
        else:
            if old.text.count(delimiter) % 2 != 0:
                raise Exception("Invalid Markdown syntax (err 0)")
            
            split_text = old.text.split(delimiter)
            
            for i in range(len(split_text)):
                if split_text[i]!="":
                    if i == 1:
                        split_node.append(TextNode(split_text[i], text_type=text_type))
                    else:
                        split_node.append(TextNode(split_text[i], TextType.TEXT))

            new_nodes.extend(split_node)

    return new_nodes
    
    
def split_nodes_image(old_nodes: list[TextNode]):
    
    new_nodes: list[TextNode] = []
    
    split_node: list[TextNode] = []
    
    node_type: TextType
    
    extracted_images: list[tuple] = []
    node_text: str = ""
    section: list[str] = []
    image_alt: str = ""
    image_link: str = ""
    
    for old in old_nodes:
        # clear list in new node
        split_node.clear()
        # extract format of this node
        node_type = old.text_type
        
        extracted_images: list[tuple] = extract_markdown_images(old.text)
        if old.text != "":
            if extracted_images == []:
                new_nodes.append(old)
            else:
                # 1. get node text
                node_text = old.text
                
                # 2. iterate over all extracted images
                for i, image in enumerate(extracted_images):
                    # 3. split text by image
                    image_alt, image_link = image[0], image[1]
                    section = node_text.split(f"![{image_alt}]({image_link})", 1)
                    
                    if i==len(extracted_images)-1:
                        if section[0]!="":
                            split_node.append(TextNode(text=section[0], text_type=node_type))
                        split_node.append(TextNode(text=image_alt, text_type=TextType.IMAGE, url=image_link))
                        if section[1]!="":
                            split_node.append(TextNode(text=section[1], text_type=node_type))
                            
                    else:
                        if section[0]!="":
                            split_node.append(TextNode(text=section[0], text_type=node_type))
                        
                        split_node.append(TextNode(text=image_alt, text_type=TextType.IMAGE, url=image_link))
                        node_text = section[1]
                        
            new_nodes.extend(split_node)
    
    return new_nodes

def split_nodes_link(old_nodes):
    
    new_nodes: list[TextNode] = []
    
    split_node: list[TextNode] = []
    
    node_type: TextType
    
    extracted_links: list[tuple] = []
    node_text: str = ""
    section: list[str] = []
    link_alt: str = ""
    link_url: str = ""
    
    for old in old_nodes:
        # clear list in new node
        split_node.clear()
        # extract format of this node
        node_type = old.text_type
        
        extracted_links: list[tuple] = extract_markdown_links(old.text)
        if old.text != "":
            if extracted_links == []:
                new_nodes.append(old)
            else:
                # 1. get node text
                node_text = old.text
                
                # 2. iterate over all extracted links
                for i, image in enumerate(extracted_links):
                    # 3. split text by image
                    link_alt, link_url  = image[0], image[1]
                    section = node_text.split(f"[{link_alt}]({link_url})", 1)
                    
                    if i==len(extracted_links)-1:
                        if section[0]!="":
                            split_node.append(TextNode(text=section[0], text_type=node_type))
                        split_node.append(TextNode(text=link_alt, text_type=TextType.LINK, url=link_url))
                        if section[1]!="":
                            split_node.append(TextNode(text=section[1], text_type=node_type))
                            
                    else:
                        if section[0]!="":
                            split_node.append(TextNode(text=section[0], text_type=node_type))
                        
                        split_node.append(TextNode(text=link_alt, text_type=TextType.LINK, url=link_url))
                        node_text = section[1]
                        
            new_nodes.extend(split_node)
    
    return new_nodes
    
    
    
    
    
    
    
