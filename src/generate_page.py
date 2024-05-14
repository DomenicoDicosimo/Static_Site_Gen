from block_markdown import markdown_to_html_node
from extract_title import extract_title
from htmlnode import (
    ParentNode,
    HTMLNode,
    LeafNode
)
import os
import shutil
from pathlib import Path


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        with open(template_path) as t:
            markdown_contents = f.read()
            template_contents = t.read()

            content = markdown_to_html_node(markdown_contents).to_html()
            title = extract_title(markdown_contents)

            template_contents = template_contents.replace("{{ Title }}",title)
            template_contents = template_contents.replace("{{ Content }}",content)

            if not os.path.exists(os.path.dirname(dest_path)):
                os.makedirs(os.path.dirname(dest_path))
            
            with open(dest_path,'w') as d:
                d.write(template_contents)
            
def generate_page_recursive(dir_path_content,template_path,dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception("Static path not found!")
    if not os.path.exists(template_path):
        raise Exception("Static path not found!")
    print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")
    
    dest_dir_path_ob = Path(dest_dir_path)

    dir_items = os.listdir(dir_path_content)
    for item in dir_items:
        dir_item_path = os.path.join(dir_path_content,item)
        dest_item_path = os.path.join(dest_dir_path,item)
        if os.path.isfile(dir_item_path):
            dir_path_item_ob = Path(dir_item_path)
            item_stem = dir_path_item_ob.stem
            html_name = f"{item_stem}.html"
            html_dest_path =  dest_dir_path_ob/ html_name
            with open(dir_item_path) as f:
                with open(template_path) as t:
                    markdown_contents = f.read()
                    template_contents = t.read()


                    content = markdown_to_html_node(markdown_contents).to_html()
                    title = extract_title(markdown_contents)

                    template_contents = template_contents.replace("{{ Title }}",title)
                    template_contents = template_contents.replace("{{ Content }}",content)
            
                    with open(html_dest_path,'w') as d:
                        d.write(template_contents)
        else:
            os.mkdir(dest_item_path)
            generate_page_recursive(dir_item_path,template_path,dest_item_path)    