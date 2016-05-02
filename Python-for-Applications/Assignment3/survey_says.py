import csv
import list_utils

print("SURVEY RESULTS");
with open('survey-results.csv') as results:
    reader = csv.reader(results, delimiter=',');
    paces=[];
    skills=[];
    for row in reader:
        pace = row[1];
        paces.append(row[1]);
        skills.append(row[2]);
    paces.remove("Pace");
    skills.remove("Skill");

    for i in range(len(paces)):
        paces[i]=int(paces[i]);
    for i in range(len(skills)):
        skills[i]=int(skills[i]);
results.close();

paceAnswers = [0,0,0,0,0];
skillAnswers = [0,0,0,0,0];
for i in range(len(paces)):
    paceAnswers[((paces[i]))-1]+=1;
for i in range(len(skills)):
    skillAnswers[((skills[i]))-1]+=1;


print("Skills \n ____");
for i in range(len(skillAnswers)):
    print(str(i+1) + ":" + str(skillAnswers[i]));
print("Average: " + str(list_utils.mean(skills)));
print("Standard Deviation: " + str(list_utils.std_dev(skills)));
print("Median: " + str(list_utils.median(skills)));


print("Paces \n ____");
for i in range(len(paceAnswers)):
    print(str(i+1) + ": " + str(paceAnswers[i]));
print("Average: " + str(list_utils.mean(paces)));
print("Standard Deviation: " + str(list_utils.std_dev(paces)));
print("Median: " + str(list_utils.median(paces)));
