from Block_markdown import *
from htmlnode import *
from inline_markdown import *

def process_inline_elements(block):
    list_of_textnodes = text_to_textnodes(block)
    html_nodes = []
    for textnode in list_of_textnodes:
        html_nodes.append(text_node_to_html_node(textnode))
    return html_nodes
def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)

    html_nodes = [

    ]
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        
        if block_type == "paragraph":
            content = process_inline_elements(block) 
            new_htmlnode = HTMLNode(tag="p", children= content)
        elif block_type == "header":
            level = block_header_level(block)
            content = process_inline_elements(block)
            new_htmlnode = HTMLNode(tag=f"h{level}", children=content)
        elif block_type == "quote":
            content = process_inline_elements(block)
            new_htmlnode = HTMLNode(tag="blockquote", children=content)
        elif block_type == "code":
            new_htmlnode = HTMLNode(tag="pre", children=[
                HTMLNode(tag="code", text=block)
            ])
        elif block_type == "list":
            new_htmlnode = HTMLNode(tag="ul" if block.is_unordered else "ol")
            for item in block.items:
                new_htmlnode.add_child(HTMLNode(tag="li", text=item))
        else:
            # Handle other block types or raise an exception for unsupported types
            raise ValueError(f"Unsupported block type: {block_type}")
        
        # Add the newly created HTML node to the list of nodes
        html_nodes.append(new_htmlnode)
    
    # Return the list of HTML nodes
    return html_nodes