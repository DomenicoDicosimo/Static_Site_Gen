import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from textnode import TextNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("sample", "sample", [], {"href": "https://www.google.com", "target": "_blank"})
        expected_output= ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

class TestLeafNode(unittest.TestCase):
    def test_none_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_output= '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), expected_output)

    def test_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_output= '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_output)

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(),expected_output)
    
    def test_eq_with_parentnode(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        ParentNode("p",[LeafNode(None, "Normal text")],)
    ],
)
        expected_output = "<p><b>Bold text</b><p>Normal text</p></p>"
        self.assertEqual(node.to_html(),expected_output)

if __name__ == "__main__":
    unittest.main()

