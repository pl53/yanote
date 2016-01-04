import os
import re
import configparser

def get_config_parser():
    config_file = "yant.cfg"
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def get_data_path():
    note_path = os.getenv("YANT_PATH")
    #note_path = "./devo_data"
    if note_path == None:
        note_path = os.path.join(os.getenv("HOME"), ".yanote")
    if not os.path.exists(note_path):
        os.makedirs(note_path)
    return note_path

def list_all_books():
    # retrive current notebooks
    note_path = get_data_path()
    all_files = os.listdir(note_path)
    db_files = [f for f in all_files if f.endswith(".db")]
    current_books = [name[:-3] for name in db_files]
    return current_books

def validate_name(pattern, name, exception_msg=""):
    if not re.match(pattern, name):
        if exception_msg == "":
            exception_msg = "'" + name + "' doesn't match required pattern " + pattern
        raise Exception(exception_msg) 

class YantException(Exception):
    def __init__(self, s):
        self.value = s
    def __str__(self):
        return str(self.value)

