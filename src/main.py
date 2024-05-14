from textnode import TextNode
from copystatic import delete_directory_contents, copy_files
from generate_page import generate_page_recursive


static_path = "./static"
public_path= "./public"

markdown_path = "./content"
template_path = "./template.html"
html_path = "./public"
            
def main():
    node = TextNode("dummy","dummy2","dummyURL")
    print(node.__repr__())

    delete_directory_contents(public_path)
    copy_files(static_path,public_path)

    generate_page_recursive(markdown_path,template_path,html_path)
main()