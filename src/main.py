from .copystatic import copy_content, public_cleanup
from .gencontent import generate_page, generate_pages_recursive

if __name__ == "__main__":
    src_path = "./static"
    dst_path = "./public"

    from_path = "content/index.md"
    template = "template.html"
    dest_path = "public/index.html"
    
    source_path = "./content"
    
    public_cleanup(dst_path)
    copy_content(src_path, dst_path)

    # generate_page(from_path, template, dest_path)
    generate_pages_recursive(source_path, template, dst_path)
