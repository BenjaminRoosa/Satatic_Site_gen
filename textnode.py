from htmlnode import *

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text="none",text_type="none_type", url= None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text != other.text :
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True
    def __repr__(self):
        print (f"TextNode({self.text}, {self.text_type}, {self.url})")

def text_node_to_html_node(Text_node):
    
    if Text_node.text_type == text_type_text:
        return LeafNode(None, value=Text_node.text)
    if Text_node.text_type == text_type_bold:
        return LeafNode("b", value=Text_node.text)
    if Text_node.text_type == text_type_italic:
        return LeafNode("i", value=Text_node.text)
    if Text_node.text_type == text_type_code:
        return LeafNode("code", value=Text_node.text)
    if Text_node.text_type == text_type_link:
        return LeafNode("a", value=Text_node.text , props={"href": Text_node.url})
    if Text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": Text_node.url, "alt": Text_node.text})
    raise ValueError(f"Invalid tect type: {Text_node.text_type}")

