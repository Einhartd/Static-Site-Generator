

class HTMLNode:

    def __init__(self, tag: str|None = None, value: str|None = None, 
                 children: list|None = None, props: dict|None = None):
        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):

        html_attrs = ""

        if self.props == None:
            return html_attrs
        
        for key in self.props:
            html_attrs += " "
            html_attrs += f"{key}="
            html_attrs += f'"{self.props[key]}"'

        return html_attrs
    
    def __repr__(self):
        return f"HTMLNode(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})"
