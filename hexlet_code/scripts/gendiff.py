import argparse
import json


def read_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)

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


    return "{\n" + "\n".join(result) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', default='plain', help='Set format of output')

    args = parser.parse_args()


    diff = generate_diff(args.first_file, args.second_file)

    print(diff)

if __name__ == '__main__':
    main()
