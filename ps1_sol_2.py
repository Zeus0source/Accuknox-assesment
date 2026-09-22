#sample json structure
students = [
    {
        "id": "S001",
        "name": "Alice Johnson",
        "grade": "10",
        "scores": {
            "math": 88,
            "english": 92,
            "science": 85,
            "history": 79
        }
    },
    {
        "id": "S002",
        "name": "Bob Smith",
        "grade": "10",
        "scores": {
            "math": 76,
            "english": 81,
            "science": 78,
            "history": 85
        }
    },
    {
        "id": "S003",
        "name": "Charlie Lee",
        "grade": "11",
        "scores": {
            "math": 90,
            "english": 87,
            "science": 91,
            "history": 88
        }
    }
]
#calculating average
avg=[]
for student in students:
    scores_stud=student["scores"]
    scores=scores_stud.values()
    avg1=sum(scores)/len(scores)
    avg.append((student["name"],avg1))
print(avg)
# seperating average scores and names 
list1, list2 = map(list, zip(*avg))
#print(list1)
#print(list2)
# ploting the bar chart
import matplotlib.pyplot as plt
plt.bar(list1,list2)
plt.xlabel("Names of Students")
plt.ylabel("Averages of Students")
plt.title("Result of students")
plt.show()