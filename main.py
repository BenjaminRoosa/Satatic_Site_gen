
from Generate_pages_r import generate_pages_recursive
import os
import shutil





def main ():

    print ("Hello world")

    
    
    print("starting ")
    if os.path.exists("src/public"):
           shutil.rmtree("src/public")
    os.makedirs("src/public")
    
    
    shutil.copytree("src/static", "src/public", dirs_exist_ok=True)
    #r_copy_static("/home/b_boosa/WorkSpace/pojects/Static Site Generator/static","/home/b_boosa/WorkSpace/pojects/Static Site Generator/public")
    
    generate_pages_recursive("src/content", "template.html", "src/public")
if __name__ == "__main__":
    main()