import re
import time
start_time = time.perf_counter()
class Timetable:
    def __init__(self, lessons):
        self.lessons = lessons
class TimetableParser:
    def parser(self, line, lesson):
        line = str(line).replace("  ", "")
        x = line.split(":")
        key = x[0]
        word = x[1].strip('\n ')
        if key == "day":
            lesson.day = word
        elif key == "time":
            lesson.time = x[1].strip('\n ') + ":" + x[2].replace("\n", "") + ":" + x[3].replace("\n", "")
        elif key == "room":
            lesson.room = word
        elif key == "lesson":
            lesson.lesson = word
        elif key == "teacher":
            lesson.teacher = word
        elif key == "location":
            lesson.location = word
        elif key == "week":
            lesson.week = word
        return lesson
    def run(self, input):
        lines = input.readlines()
        lessons = [Atfirst(), Atfirst(), Atfirst(), Atfirst(), Atfirst(), Atfirst(), Atfirst(),Atfirst()]
        i = -1
        global cnt
        cnt = 0
        for line in lines:
            line = line.replace("\n", "")
            line = line.replace("  ", "")
            if re.fullmatch(r"\s*lesson\d:", line) is not None:
                i += 1
                cnt += 1
            elif line.count("timetable") != 1:
                lessons[i] = self.parser(line, lessons[i])
        schedule = Timetable(lessons)
        return schedule
class Atfirst:
    def __init__(self):
        self.day = None
        self.time = None
        self.room = None
        self.lesson = None
        self.teacher = None
        self.location = None
        self.week = None
    
input = open("timetable.yaml", "r", encoding="utf-8")
output = open("timetable.json", "w", encoding="utf-8")
start_time = time.perf_counter()
parser = TimetableParser()
schedule = parser.run(input)
json = "{\n\"timetable\": {\n"
for i in range(cnt):
    el = schedule.lessons[i]
    json += "\t\"lesson{}\": {{\n".format(i+1)
    sub_dict = schedule.lessons[i].__dict__
    for p in sub_dict:
        if(p == "week"):
            json += "\t\t\"{}\": \"{}\"\n".format(p, sub_dict[p], p)
        else: 
            json += "\t\t\"{}\": \"{}\",\n".format(p, sub_dict[p], p)
    if(i + 1 < cnt):
        json += "\t\t}},\n".format(i+1) 
    else:
        json += "\t\t}}\n".format(i+1) 
json += "\t}\n}"  
output.write(json)
input.close()
output.close()
print(time.perf_counter() - start_time)

