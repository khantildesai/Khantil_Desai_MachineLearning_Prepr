import csv
import matplotlib.pyplot as plt

fill = []
with open("filler.txt") as filler:
    for line in filler:
        fill.append(line.replace("\n", ""))

punctuation = []
with open("filler.txt") as punc:
    for line in punc:
        punctuation.append(line.replace("\n", ""))

with open("job_skills.csv") as job_skills: #puts jobs into dict with category as key and list of skills as values
    readCSV = csv.reader(job_skills, delimiter=',')
    jobs = dict()
    for row in readCSV:
        category = row[2]
        skills = row[5]
        for word in fill:
            skills = skills.replace(word, " ")
        if category not in jobs.keys():
            jobs.update({category:str()})
            jobs[category] += skills
        else:
            jobs[category] += " " + skills

for i in jobs.values():
    for p in punctuation:
        i.replace(p, "")

for i in jobs.keys():
    new_value = []
    jobs[i].replace("  ", "")
    jobs[i] = jobs[i].split()
    for j in jobs[i]:
        new_value.append([j, jobs[i].count(j)])
    jobs[i] = new_value
    new_value = []
    for skill in jobs[i]:
        if len(new_value) < 5:
            new_value.append(skill)
        else:
            min = 0
            for item in new_value:
                if item[1] > min:
                    min = item[1]
            for item in new_value:
                if item[1] == min:
                    item = skill
    jobs[i] = new_value

for i in jobs.keys():
    new_labels = []
    new_count = []
    for j in jobs[i]:
        new_labels.append(j[0])
        new_count.append(j[1])
    jobs[i] = [new_labels, new_count]

for i in jobs.keys():
    vals = jobs[i][1]
    lab = jobs[i][0]

    plt.axis("equal")
    plt.pie(x=vals, labels=lab)
    plt.show()
    #plt.savefig(f"charts/{i}.svg")