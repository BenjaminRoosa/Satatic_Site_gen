from Block_markdown import *

from inline_markdown import *

def process_inline_elements(block):
    list_of_textnodes = text_to_textnodes(block)
    html_nodes = []
    for textnode in list_of_textnodes:
        html_nodes.append(text_node_to_html_node(textnode))
    return html_nodes
def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)

    root_html_node = ParentNode(tag="div")
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        
        if block_type == "paragraph":
            content = process_inline_elements(block) 
            new_htmlnode = ParentNode(tag="p", children= content)
        elif block_type == "header":
            level = block_header_level(block)
            content = process_inline_elements(block.lstrip("# ").strip())
            new_htmlnode = ParentNode(tag=f"h{level}", children=content)
        elif block_type == "quote":
            content = process_inline_elements(block.lstrip("> "))
            new_htmlnode = ParentNode(tag="blockquote", children=content)
        elif block_type == "code":
            new_htmlnode = ParentNode(tag="pre", children=[
                ParentNode(tag="code", children=[LeafNode(tag=None, value=block)])
            ])
        elif block_type == "unordered_list" or block_type == "ordered_list":
            list_tag = "ol" if block_type == "ordered_list" else "ul"
            new_htmlnode = ParentNode(tag=list_tag)
            if block_type == "ordered_list":
                ordered_block = block.split('\n')
                for i in range(len(ordered_block)):
                    list_item_content = process_inline_elements(ordered_block[i].lstrip(f"{i+1}. ").strip())
                    new_htmlnode.add_child(ParentNode(tag="li", children= list_item_content))
            else:
                for item in block.split('\n'):
                    list_item_content = process_inline_elements(item.lstrip("*-").strip())
                    new_htmlnode.add_child(ParentNode(tag="li", children= list_item_content))

        else:
            # Handle other block types or raise an exception for unsupported types
            raise ValueError(f"Unsupported block type: {block_type}")
        
        # Add the newly created HTML node to the list of nodes
        root_html_node.add_child(new_htmlnode)
    
    # Return the list of HTML nodes
    return root_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith('# '):
            print(block.lstrip('# ').strip())
            return block.lstrip('# ').strip()
    raise Exception("No h1 header found in the markdown file")


