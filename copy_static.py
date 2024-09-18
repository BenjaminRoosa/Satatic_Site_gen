from os import(
    mkdir,
    listdir,
    makedirs,
    rename
)
from os.path import(
    exists,
    join,
    isfile,
    dirname
)
from shutil import *
from block_to_HTML import*

def r_copy_static(source_dir, destination_dir):
    if exists(destination_dir):
        rmtree(destination_dir)
    
    mkdir(destination_dir)
     
    
    dir_list = listdir(source_dir)
        
    for dir in dir_list:
            full_source = join(source_dir, dir)
            full_destination = join(destination_dir, dir)
           
            if isfile(full_source):
                
                copy(full_source, full_destination)
            else:
                
                r_copy_static(full_source, full_destination)
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    page_markdown = ''
    
    template_text= ''
    if dest_path.endswith('.md'):
        dest_path = dest_path[:-3] + '.html'
    try:
        print(f"from_path: {from_path}, type: {type(from_path)}")
        with open(from_path, 'r', encoding="utf-8") as markdown_file:
            page_markdown = markdown_file.read()
    
    
        with open(template_path, 'r', encoding="utf-8") as template_file:
            template_text = template_file.read()
            print(f"print {template_file}")
    except TypeError as e:
        print(f"Error opening {from_path}: {e}") 
    html_tree = markdown_to_html_node(page_markdown)

    new_html = html_tree.to_html()
    
    
    markdown_title = extract_title(page_markdown)
    template_text = template_text.replace("{{ Title }}",markdown_title)
    final_text = template_text.replace("{{ Content }}",f"{new_html}")
    if  not exists(dirname(dest_path)):
        makedirs(dirname(dest_path))
    
    with open(dest_path,  "w", encoding="utf-8") as HTML_page:
        HTML_page.write(final_text)
        
    