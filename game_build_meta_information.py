import json


def update(initial_meta, command, namespace, values, type_=1):
    if command == "append":
        if namespace not in initial_meta:
            initial_meta[namespace] = {}
        if type_ not in initial_meta[namespace]:
            initial_meta[namespace][type_] = []

        for value in values:
            if value not in initial_meta[namespace][type_]:
                initial_meta[namespace][type_].append(value)

    elif command == "delete":
        if namespace in initial_meta and type_ in initial_meta[namespace]:
            for value in values:
                if value in initial_meta[namespace][type_]:
                    initial_meta[namespace][type_].remove(value)


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)