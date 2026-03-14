from copystatic import copy_content, public_cleanup

if __name__ == "__main__":
    src_path = "./static"
    dst_path = "./public"
    
    public_cleanup(dst_path)
    copy_content(src_path, dst_path)