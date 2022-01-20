import time, json, yaml

start_time = time.perf_counter()
with open("timetable1.json", "w", encoding="utf-8") as output:
    with open("timetable.yaml", "r", encoding="utf-8") as input:
        yaml_object = yaml.safe_load(input)
        json.dump(yaml_object, output, ensure_ascii=False, indent=1)


print(time.perf_counter() - start_time)