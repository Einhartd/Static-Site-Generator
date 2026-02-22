import re

def extract_markdown_images(text: str):
    images: list[tuple] | None = []
    matches = re.findall(r'!\[(.+?)\]\((.+?)\)', text)
    return matches

def extract_markdown_links(text: str):
    links: list[tuple] | None = []
    matches = re.findall(r'(?<!!)\[(.+?)\]\((.+?)\)', text)
    return matches
