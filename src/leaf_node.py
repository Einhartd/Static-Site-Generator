from html_node import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str|None = None, value: str|None = None,
                props: dict|None = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return self.value
        else:
            html_attrs: str = self.props_to_html()
            return f"<{self.tag}{html_attrs}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag = {self.tag}, value = {self.value}, props = {self.props})"
    
