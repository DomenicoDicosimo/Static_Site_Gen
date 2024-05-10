from htmlnode import LeafNode
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if(self.text == other.text):
            if(self.text_type == other.text_type):
                if(self.url == other.url):
                    return True
                
    def __repr__(self):
        return f"Textnode('{self.text}', '{self.text_type}', '{self.url}')"

    def text_node_to_html_node(text_node):
        if text_node.text_type == "text":
            text_node = LeafNode(None,text_node.text)
        elif text_node.text_type == "bold":
            text_node = LeafNode("b",text_node.text)
        elif text_node.text_type == "italic":
            text_node = LeafNode("i",text_node.text)
        elif text_node.text_type == "code":
            text_node = LeafNode("code",text_node.text)
        elif text_node.text_type == "link":
            text_node = LeafNode("a",text_node.text,None,{"href":text_node.url})
        elif text_node.text_type == "image":
            text_node = LeafNode("img","",[],{"href":text_node.url,"alt":text_node.text})
        else:
            raise Exception("What the heck kind of textnode is this!")
