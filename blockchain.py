import os
import hashlib

from os import walk

dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'blocks')


def _write_to_file(file_name, sender, receiver, amount, description, hashed=None):
    with open(file_name, "w") as file:
        if hashed:
            file.write(hashed + "\n\n")
        file.write("sender: " + sender)
        file.write("\nreceiver: " + receiver)
        file.write("\namount: " + amount)
        file.write("\ndescription: " + description)


def get_all_blocks(path: str) -> list:
    file_list = []
    for (dirpath, dirnames, filenames) in walk(path):
        file_list.extend(filenames)
        break
    file_list = [x for x in file_list if x.startswith("block")]
    file_list.sort()
    return file_list


def create_new_block(sender: str, receiver: str, amount: str, description: str):

    file_list = get_all_blocks(dir_path)

    if "block 1.txt" not in file_list:
        file_name = os.path.join(dir_path, "block 1.txt")
        _write_to_file(file_name, sender, receiver, amount, description)
    else:
        file = open(os.path.join(dir_path, file_list[-1]), "r")
        content = file.read()
        file.close()
        hashed = hashlib.sha256(bytes(content, "utf-8")).hexdigest()
        number_of_block = file_list[-1].split(".")[0]
        number_of_block = int(number_of_block.split()[1])
        file_name = os.path.join(dir_path, "block {}.txt".format(number_of_block+1))
        _write_to_file(file_name, sender, receiver, amount, description, hashed)


def mine():
    file_list = get_all_blocks(dir_path)
    for i in range(1, len(file_list)):
        prev_file = open(os.path.join(dir_path, file_list[i-1]))
        prev_content = prev_file.read()
        prev_content = hashlib.sha256(bytes(prev_content, "utf-8")).hexdigest()
        prev_file.close()
        next_file = open(os.path.join(dir_path, file_list[i]))
        next_content_hash = next_file.readline()[:-1]
        if prev_content != next_content_hash:
            return [False, len(file_list)]
    return [True, len(file_list)]
