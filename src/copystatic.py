import os
import shutil

def public_cleanup(dst_path):
    if not os.path.exists(dst_path):
        # if not create one
        os.mkdir(dst_path)
    else:
        # delete contents from dst dir and create new
        shutil.rmtree(dst_path)
        os.mkdir(dst_path)

def copy_content(src_path, dst_path):

    if os.listdir(src_path):
        for item in os.listdir(src_path):
            # if item is file copy
            filepath = os.path.join(src_path, item)
            if os.path.isfile(filepath):
                #copy
                shutil.copy(filepath, dst_path)
                print(f"Copied file: {filepath} to: {dst_path}")
            else:
                #create folder in dst with item name
                dir_filepath = os.path.join(dst_path, item)
                os.mkdir(dir_filepath)
                #recursive
                copy_content(filepath, dir_filepath)
    else:
        return
