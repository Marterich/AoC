example = [l.strip().split() for l in open("example.txt")] 
input = [l.strip().split() for l in open("input.txt")] 

def build_structure (data):
    folder_structure = {"/":0}
    current_path = ""
    for line in data:
        # print(f"{line=}")
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                match line[2]:
                    case "..":
                        current_path = current_path[:current_path.rindex("/")] # Move the current Path up one directory by finding the last "/" in the path
                    case "/":
                        current_path = "/"
                    case _:
                        current_path += "/" + line[2]
                        folder_structure[current_path] = 0
        else:
            if line[0].isdigit(): # If a File is found, Update the size of all the parent directories
                temp_path = current_path
                while temp_path != "":
                    folder_structure[temp_path] += int(line[0])
                    temp_path = temp_path[:temp_path.rindex("/")]
    return folder_structure


def part1(input_data, max_size = 100000):
    directories = build_structure(input_data)
    ret = 0
    for size in directories.values():
        if size < max_size:
            ret += size
    return ret

def part2(input_data, total_space = 70000000, space_needed = 30000000):
    directories = build_structure(input_data)
    additional_space_needed = space_needed - (total_space - directories["/"])
    deletion_candidate = ["",0]
    for dir,size in directories.items():
        if size < additional_space_needed:
            pass
        else:
            if deletion_candidate[1] == 0 or size < deletion_candidate[1]:
                deletion_candidate = [dir,size]
    return deletion_candidate[1]


assert (part1(example)) == 95437
assert (part1(input)) == 1844187
assert (part2(example)) == 24933642
assert (part2(input)) == 4978279