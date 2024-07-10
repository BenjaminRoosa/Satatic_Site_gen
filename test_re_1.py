
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
)
from inline_markdown import(
    split_nodes_image,
    split_nodes_link,
)
#def main():
# Testing
#    node = TextNode(
#    "This is a link to [Google](https://google.com) and another [link](https://example.com)",
#    text_type_text,
#    )      

#    new_nodes = split_nodes_link([node])

#    for n in new_nodes: 
#        print(f"text: {n.text}, text_type: {n.text_type}, url: {n.url}")
#main()
# Expected output:
# text: This is a link to , text_type: text, url: None
# text: Google, text_type: link