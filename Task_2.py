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


with open("Task_2_json_file_example.json", "r") as file:
    meta = json.load(file)

update(meta, "append", "GTL::Build::Tags", ["DX13", "Uplay", "DLSS"], 1)
update(meta, "delete", "GTL::Build::Categories", "NODRM")

with open("Task_2_json_file_example.json", "w") as file:
    json.dump(meta, file, indent=2)
