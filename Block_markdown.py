block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split('\n\n')
    blocks = [block.strip() for block in raw_blocks if block.strip()]
    return blocks

def does_every_line_start_with(block, startchar):
    for i in block.split("\n"):
        if not (i.startswith(startchar)):
            return False
    return True

def is_ordered_list(block):
    block_lines = block.split('\n')
    for i, line in enumerate(block_lines, start=1):
        if not line.startswith(f"{i}. "):
            return False
    return True
def block_to_block_type(block):
    
    
    #heading
    for level in range(1, 7):
        if block.startswith("#" * level + " "):
            return block_type_heading
        
    #code
    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    #quote
    if does_every_line_start_with(block, ">"):
        return block_type_quote
    
    #unordered_list
    if does_every_line_start_with(block,"* ") or does_every_line_start_with(block,"- "):
        return block_type_unordered_list
    #ordered_list
    
    if is_ordered_list(block):
        return block_type_ordered_list


    return block_type_paragraph