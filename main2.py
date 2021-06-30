import os


def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                file_list.append(os.path.join(root, file))
    return file_list

def create_result_file(path):
    file_dict = {}
    file_list = get_file_list(path)
    for file in file_list:
        with open(file, encoding="utf-8") as some_txt:
            file_dict[file] = len(some_txt.readlines())
    sorted_files_tuple = sorted(file_dict.items(), key=lambda x: x[1])
    sorted_files_dict = dict(sorted_files_tuple)

    for sorted_file in sorted_files_dict:
        with open(sorted_file, 'r', encoding="utf-8") as data:
            text = data.read()
            with open('result.txt', 'a', encoding="utf-8") as result:
                result.write(sorted_file)
                result.write('\n')
                result.write(str(sorted_files_dict[sorted_file]))
                result.write('\n')
                result.write(text)
                result.write('\n')
    return None


create_result_file('Examples/')


