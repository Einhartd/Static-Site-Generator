from .html_node import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str|None = None, value: str|None = None,
                props: dict|None = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag is None:
            if self.value is None:
                raise ValueError
            return self.value

        html_attrs = self.props_to_html()

        if self.tag == "img":
            return f"<img{html_attrs}>"

        if self.value is None:
            raise ValueError

        return f"<{self.tag}{html_attrs}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag = {self.tag}, value = {self.value}, props = {self.props})"
    
