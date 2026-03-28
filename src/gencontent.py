import re
import os
import shutil
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

def generate_page(from_path, template_path, dest_path, basepath):
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

    # replacement with basepath
    template_file_read = template_file_read.replace('href="/', f'href="{basepath}')
    template_file_read = template_file_read.replace('src="/', f'src="{basepath}')

    dir_path = os.path.dirname(dest_path)
    if dir_path != "":
        os.makedirs(dir_path, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template_file_read)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print(f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}")
    
    if os.listdir(dir_path_content):
        for item in os.listdir(dir_path_content):
            # get filepath of item
            filepath = os.path.join(dir_path_content, item)
            if os.path.isfile(filepath):
                # prepare destination filepath
                # get item name, cut format after '.' and change it to html
                page_name_list = item.split('.')
                if page_name_list and len(page_name_list)>1:
                    page_name_list[-1] = "html"
                    page_html = ".".join(page_name_list)
                    # generate .html page from found file
                    dest_path = os.path.join(dest_dir_path, page_html)
                    generate_page(filepath, template_path, dest_path, basepath)
                    print(f"Generated page from {filepath} to: {dest_dir_path}")
            else:
                # create folder in dest dir
                dir_filepath = os.path.join(dest_dir_path, item)
                if not os.path.isdir(dir_filepath): 
                    os.mkdir(dir_filepath)
                # recursive call
                generate_pages_recursive(filepath, template_path, dir_filepath, basepath)