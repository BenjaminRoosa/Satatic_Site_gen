import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    
    pattern = r"\[([^]]+)]\(([^)]+)\)"
    return re.findall(pattern, text)

