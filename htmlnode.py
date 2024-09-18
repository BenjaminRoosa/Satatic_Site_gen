class HTMLNode:
    def __init__(self, tag= None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props
    
    def add_child(self, new_html_node):
        self.children.append(new_html_node)
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        html_string = ""
        if self.props == None:
            html_string = ""
            return html_string
        
        for prop in self.props:
            html_string += f' {prop}="{self.props[prop]}"'
        
        return html_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.tag is "h1":
            return ""
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        if self.tag is "h1":
            return ""
        children_html = ""
        for child in self.children:
            if isinstance(child, str):
                children_html += child
            elif isinstance(child, HTMLNode):
                children_html += child.to_html()
            else:
                raise ValueError(f"Invalid child type: {type(child)}")
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
