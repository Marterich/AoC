"""
Advend of Code 2022
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7

The input are cd (Change Directory) and ls (list) commands followed by their output. 
"""
example = [l.strip().split() for l in open("example.txt", encoding="utf-8")]
challenge = [l.strip().split() for l in open("challenge.txt", encoding="utf-8")]

def build_structure (data):
    """
    Parse the Input Files into a workable dictionary with the folder path as the key
    and the folder size as the value
    """
    folder_structure = {"/":0}
    current_path = ""
    for line in data:
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                match line[2]:
                    case "..":
                        # Move the current Path up one directory by finding the last "/" in the path
                        current_path = current_path[:current_path.rindex("/")]
                    case "/":
                        current_path = "/"
                    case _:
                        current_path += "/" + line[2]
                        folder_structure[current_path] = 0
        else:
            if line[0].isdigit():
                # If a File is found, Update the size of all the parent directories
                temp_path = current_path
                while temp_path != "":
                    folder_structure[temp_path] += int(line[0])
                    temp_path = temp_path[:temp_path.rindex("/")]
    return folder_structure


def part1(challenge_data, max_size = 100000):
    """
    Find all of the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?
    """
    directories = build_structure(challenge_data)
    ret = 0
    for size in directories.values():
        if size < max_size:
            ret += size
    return ret

def part2(challenge_data, total_space = 70000000, space_needed = 30000000):
    """
    Find the smallest directory that, if deleted, would free up enough space on the 
    filesystem to run the update. What is the total size of that directory?
    """
    directories = build_structure(challenge_data)
    additional_space_needed = space_needed - (total_space - directories["/"])
    deletion_candidate = ["",0]
    for path,size in directories.items():
        if size < additional_space_needed:
            pass
        else:
            if deletion_candidate[1] == 0 or size < deletion_candidate[1]:
                deletion_candidate = [path,size]
    return deletion_candidate[1]


assert (part1(example)) == 95437
print(f"{part1(challenge)=}")
assert (part2(example)) == 24933642
print(f"{part2(challenge)=}")
