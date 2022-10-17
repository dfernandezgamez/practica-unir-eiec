"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Can't order {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    items = list(dict.fromkeys(items))
    return items


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    order_ascending = DEFAULT_ASCENDING
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        order_ascending = sys.argv[3].lower() == "yes"
    else:
        print("A file must be provided as first argument")
        print("Use the second argument if you want to delete duplicates")
        print("Use third argument for sorting order")
        sys.exit(1)

    print(f"Words will be read from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File {filename} do not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, order_ascending))
