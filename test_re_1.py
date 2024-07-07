#import unittest
from re_1 import (
    extract_markdown_images, extract_markdown_links
    )

def main():
    text_with_images = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    text_with_links = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    text_with_no_markdown = "This text has no markdown links or images."

    print("Extracted Images:", extract_markdown_images(text_with_images))
    print("Extracted Links:", extract_markdown_links(text_with_links))
    print("Extracted from No Markdown:", extract_markdown_images(text_with_no_markdown), extract_markdown_links(text_with_no_markdown))

main()