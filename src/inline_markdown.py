from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)
import re



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
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_images(old_node.text)
        if not matches:
            new_nodes.append(old_node)
            continue
        temp_split = []
        split_nodes = []
        original_text = ""
        for tup in matches:
            if temp_split == []:
                temp_split = old_node.text.split(f"![{tup[0]}]({tup[1]})", 1)
                if temp_split[0] != "":
                    split_nodes.append(TextNode(temp_split[0],text_type_text))
                split_nodes.append(TextNode(tup[0], text_type_image,tup[1]))
            else:
                temp_split = temp_split[1].split(f"![{tup[0]}]({tup[1]})", 1)
                if temp_split[0] != "":
                    split_nodes.append(TextNode(temp_split[0],text_type_text))
                split_nodes.append(TextNode(tup[0], text_type_image,tup[1]))
            original_text = temp_split[1]
        if original_text != "":
            split_nodes.append(TextNode(original_text, text_type_text))
        new_nodes.extend(split_nodes)     
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_links(old_node.text)
        if not matches:
            new_nodes.append(old_node)
            continue
        temp_split = []
        split_nodes = []
        for tup in matches:
            if temp_split == []:
                temp_split = old_node.text.split(f"[{tup[0]}]({tup[1]})", 1)
                if temp_split[0] != "":
                    split_nodes.append(TextNode(temp_split[0],text_type_text))
                split_nodes.append(TextNode(tup[0], text_type_link,tup[1]))
            else:
                temp_split = temp_split[1].split(f"[{tup[0]}]({tup[1]})", 1)
                if temp_split[0] != "":
                    split_nodes.append(TextNode(temp_split[0],text_type_text))
                split_nodes.append(TextNode(tup[0], text_type_link,tup[1]))
            original_text = temp_split[1]
        if original_text != "":
            split_nodes.append(TextNode(original_text, text_type_text))
        new_nodes.extend(split_nodes)    
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def text_to_textnodes(text):
    temp_node = TextNode(text,text_type_text)
    newlist = [temp_node]
    newlist = split_nodes_delimiter(newlist,"**",text_type_bold)
    newlist = split_nodes_delimiter(newlist,"*",text_type_italic)
    newlist = split_nodes_delimiter(newlist,"`",text_type_code)
    newlist = split_nodes_image(newlist)
    newlist = split_nodes_link(newlist)
    return newlist
