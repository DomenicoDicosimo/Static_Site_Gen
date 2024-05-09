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
        pass