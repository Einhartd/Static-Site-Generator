import re
import os
from .markdown_to_html_node import markdown_to_html_node
from .parent_node import ParentNode

def extract_title(markdown: str) -> str:
    title_regex = r'^#\s'
    lines = markdown.split('\n')
    for line in lines:
        match = re.search(title_regex, line)
        if match:
            return line[match.span()[1]:]
    raise Exception("No h1 found.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path) as f:
        md_file_read = f.read()

    with open(template_path) as f:
        template_file_read = f.read()

    md_html_node: ParentNode  = markdown_to_html_node(md_file_read)

    md_html_str: str = md_html_node.to_html()
    page_title = extract_title(md_file_read)

    template_file_read = template_file_read.replace("{{ Title }}", page_title)
    template_file_read = template_file_read.replace("{{ Content }}", md_html_str)

    dir_path = os.path.dirname(dest_path)
    if dir_path != "":
        os.makedirs(dir_path, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template_file_read)