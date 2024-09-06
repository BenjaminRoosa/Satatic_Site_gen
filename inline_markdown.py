
from textnode import *


from re_1 import( 
    extract_markdown_links, extract_markdown_images
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
def split_nodes_image(old_nodes):
    new_nodes = []
    
    for old_node in old_nodes:
        image_tups = extract_markdown_images(old_node.text)
        if not image_tups:
            new_nodes.append(old_node)
            continue
        working_section = old_node.text
        for desc, url in image_tups:
            new_section = working_section.split(f"![{desc}]({url})", 1)
            if new_section[0]:
                new_nodes.append(TextNode(new_section[0], text_type_text))
            new_nodes.append(TextNode(desc, text_type_image, url))
            working_section = new_section[1]
        #if working_section:
        #    new_nodes.append(TextNode(working_section, text_type_text))
    return new_nodes
            
        
        
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        link_tups = extract_markdown_links(old_node.text)
        if not link_tups:
            new_nodes.append(old_node)
            continue
        working_section = old_node.text
        for desc, url in link_tups:
            new_section = working_section.split(f"[{desc}]({url})", 1)
            if new_section[0]:
                new_nodes.append(TextNode(new_section[0], text_type_text))
            new_nodes.append(TextNode(desc, text_type_link, url))
            working_section = new_section[1]
        if working_section:
            new_nodes.append(TextNode(working_section, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    #create first text_node
    working_section = [TextNode(text, text_type_text)]
    #finall_section = []
    #completed_steps = 0
    
    #extract bold
    #bold_extract_complet = False
    bold_section_two = split_nodes_delimiter(working_section, "**", text_type_bold)
    #if len(working_section) == len(bold_section_two):
        #bold_extract_complet = True
        
    #extract italic
    #italic_extract_complet = False
    italic_section_three = split_nodes_delimiter(bold_section_two, "*", text_type_italic)
    #if len(bold_section_two) == len(italic_section_three):
        #italic_extract_complet = True
    
    #extract code
    #code_extract_complet = False
    code_section_four = split_nodes_delimiter(italic_section_three, "`", text_type_code)
    #if len(italic_section_three) == len(code_section_four):
        #code_extract_complet = True
    
    #extract links
    #links_extract_complet = False
    links_section_five = split_nodes_link(code_section_four)
    #if len(code_section_four) == len(links_section_five):
        #links_extract_complet = True
        
    #extract images
    #images_extract_complet = False
    images_section_six = split_nodes_image(links_section_five)
    #if len(links_section_five) == len(images_section_six):
        #images_extract_complet = True
    #if bold_extract_complet and italic_extract_complet and code_extract_complet and links_extract_complet and images_extract_complet:
        #finall_section = images_section_six
        #completed_steps = 1
    #else:
        #working_section = images_section_six
    return images_section_six
