import sys

from .copystatic import copy_content, public_cleanup
from .gencontent import generate_pages_recursive

if __name__ == "__main__":

    basepath: str = ""

    if len(sys.argv) >= 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"


    src_path = "./static"
    dst_path = "./docs"

    from_path = "content/index.md"
    template = "template.html"
    dest_path = "docs/index.html"
    
    source_path = "./content"
    
    public_cleanup(dst_path)
    copy_content(src_path, dst_path)

    generate_pages_recursive(source_path, template, dst_path, basepath)
