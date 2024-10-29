import json
import yaml

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_diff(file1, file2):
    if file1.endswith('.yml') or file1.endswith('.yaml'):
        data1 = read_yaml(file1)
    else:
        data1 = read_json(file1)

    if file2.endswith('.yml') or file2.endswith('.yaml'):
        data2 = read_yaml(file2)
    else:
        data2 = read_json(file2)

    all_keys = sorted(data1.keys() | data2.keys())
    result = []

    for key in all_keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            result.append(f"    {key}: {data1[key]}")
        else:
            result.append(f"  - {key}: {data1[key]}")
            result.append(f"  + {key}: {data2[key]}")

    output = "{\n" + "\n".join(result) + "\n}"
    output = output.replace("True", "true").replace("False", "false")

    return output
