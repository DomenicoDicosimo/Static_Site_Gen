import os
import shutil

static_path = "/home/dom/workspace/static_folders/Static_Site_Gen"
public_path= "/home/dom/workspace/github.com/DomenicoDicosimo/Static_Site_Gen/public"

def delete_directory_contents(path):
    if not os.path.isdir(path):
        raise ValueError("Specified path is not a directory")    
    for item_name in os.listdir(path):
        item_path = os.path.join(path, item_name)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

def copy_files(src_path = "", target_path=""):
    if not os.path.exists(src_path):
        raise Exception("Static path not found!")
    if not os.path.exists(target_path):
        raise Exception("Public path not found!")
    
    dir_items = os.listdir(src_path)
    for item in dir_items:
        src_item_path = os.path.join(src_path, item)
        target_item_path = os.path.join(target_path, item)
        if os.path.isfile(src_item_path):
            shutil.copy(src_item_path,target_item_path)
        else:
            os.mkdir(target_item_path)
            copy_files(src_item_path,target_item_path)