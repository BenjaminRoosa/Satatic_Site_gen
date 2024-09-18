from copy_static import generate_page

from os import(
    listdir,
    makedirs
)
from os.path import(
    join,
    isfile,
    exists
)
from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    
    if isfile(dir_path_content):
         
        generate_page(dir_path_content, template_path, dest_dir_path)
    else:
        contents = listdir(dir_path_content)
        for i in contents:
            content_path_to_i = join(dir_path_content, i)
            dest_dir_path_to_i = join(dest_dir_path, i)

            if not isfile(content_path_to_i):
                 makedirs(dest_dir_path_to_i, exist_ok=True)
        
            
            generate_pages_recursive(content_path_to_i, template_path, dest_dir_path_to_i)