from textnode import TextNode, TextType


if __name__ == "__main__":
    text_node = TextNode("This is some anchor text", TextType.LINK, url = "https://www.boot.dev")
    print(text_node)