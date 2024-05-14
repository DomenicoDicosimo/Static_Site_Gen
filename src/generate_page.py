from block_markdown import markdown_to_html_node
from extract_title import extract_title
from htmlnode import (
    ParentNode,
    HTMLNode,
    LeafNode
)
import os


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
            




