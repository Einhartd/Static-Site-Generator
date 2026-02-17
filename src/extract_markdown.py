import re

def extract_markdown_images(text):
    images: list[tuple] | None = []
    matches = re.findall(r'!\[(.+?)\]\((.+?)\)', text)
    return matches

def extract_markdown_links(text):
    links: list[tuple] | None = []
    matches = re.findall(r'\[(.+?)\]\((.+?)\)', text)
    return matches
