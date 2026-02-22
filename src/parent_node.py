from .html_node import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list, props: dict|None = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        
        if self.tag == None:
            raise ValueError("No tag value found")
        
        if self.children == None or len(self.children)==0:
            raise ValueError("No children found")
        
        md_text = ""
        md_text += f"<{self.tag}"

        if self.tag:
            props_attrs: str = self.props_to_html()
            md_text += f"{props_attrs}"
        
        md_text += f">"

        for child in self.children:
            md_text += child.to_html()

        md_text += f"</{self.tag}>"

        return md_text
    
    def __repr__(self):
        return f"ParentNode(tag = {self.tag}, children = {self.children}, props = {self.props})"
    