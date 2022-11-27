import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]: # TODO реализовать конвертер из csv в json
    with open(filename, 'r') as f:
        whole_file = f.read().split(new_line)
        header = whole_file[0].split(delimiter)
        data = whole_file[1:len(whole_file)]
        out_list = []
        for line in data:
            res = {header[i]: line.split(delimiter)[i] for i in range(len(header))}
            out_list.append(res)
        return out_list

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
