from htmlnode import (
    ParentNode,
    HTMLNode,
    LeafNode
)
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    stripped = list(filter(None,map(lambda x: x.strip(), markdown.split("\n\n"))))
    return stripped

def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ") 
        or block.startswith("## ") 
        or block.startswith("### ") 
        or block.startswith("#### ") 
        or block.startswith("##### ") 
        or block.startswith("###### ")
        ):
        return block_type_heading
    elif block.startswith("```") and block.endswith("```"):
        return block_type_code
    elif block.startswith(">"):
        count = 0
        for line in lines:
            if line.startswith(">"):
                count += 1
            else:
                return block_type_paragraph
        if count == len(lines):
            return block_type_quote
    elif block.startswith("* ") or block.startswith("- "):
        count = 0
        for line in lines:
            if line.startswith("* ") or line.startswith("- "):
                count += 1
            else:
                return block_type_paragraph
        if count == len(lines):
            return block_type_ulist
    elif block.startswith("1. "):
        count = 0
        nums = 0
        for line in lines:
            count += 1
            if line.startswith(f"{count}. "):
                nums += 1
            else:
                return block_type_paragraph
        if nums == len(lines):
            return block_type_olist
    else:
        return block_type_paragraph

def code_block_to_HTMLNode(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid Code block")
    text = block[4:-3]
    children = text_to_child(text)
    code = ParentNode("code", children)
    return ParentNode("pre",[code])
    
def quote_block_to_HTMLNode(block):
    lines = block.split("/n")
    new_lines = {}
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_child(content)
    return ParentNode("blockquote", children)
    
def ulist_block_to_HTMLNode(block):
    items = block.split("\n")
    html_items = []
    for line in items:
        text = line[2:]
        children = text_to_child(text)
        html_items.append(ParentNode("li",children))
    return ParentNode("ul",html_items)
    
def olist_block_to_HTMLNode(block):
    items = block.split("\n")
    html_items = []
    for line in items:
        text = line[3:]
        children = text_to_child(text)
        html_items.append(ParentNode("li",children))
    return ParentNode("ol",html_items)

def heading_block_to_HTMLNode(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_child(text)
    return ParentNode(f"h{level}",children)
    
def paragraph_block_to_HTMLNode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_child(paragraph)
    return ParentNode("p",children)

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    children = []
    for block in block_list:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div",children,None)

def text_to_child(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
        

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_block_to_HTMLNode(block)
    if block_type == block_type_heading:
        return heading_block_to_HTMLNode(block)
    if block_type == block_type_code:
        return code_block_to_HTMLNode(block)
    if block_type == block_type_olist:
        return olist_block_to_HTMLNode(block)
    if block_type == block_type_ulist:
        return ulist_block_to_HTMLNode(block)
    if block_type == block_type_quote: 
        return quote_block_to_HTMLNode(block)
    raise ValueError("Invalid block type")
            