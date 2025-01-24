list1 = ["Cohort24","Cohort23","Cohort22"]
list2 = ["4 months","5 months","6 months"]
cohort_details = zip(list1, list2)

##

my_dict = {'name': 'Gloria', 'age': 12}
new_data = {'city': 'Yaba', 'age': 13}

for key,value in new_data.items():
    my_dict[key] = value


##

semicolon = {
    'Cohort': [24, 23, 22, 21],
    'Duration': ['4m', '5m', '6m', '7m']
}

##

school_records = {
    'Class_1': {
        'Students': [
            {'name': 'Harry', 'scores': {'Math': 88, 'English': 76}},
            {'name': 'Solomon', 'scores': {'Math': 95, 'English': 89}}
        ]
    },
    'Class_2': {
        'Students': [
            {'name': 'Daniel', 'scores': {'Math': 78, 'English': 72}},
            {'name': 'Samuel', 'scores': {'Math': 85, 'English': 80}}
        ]
    }
}

class_1 = school_records['Class_1']['Students']
math_score_1 = sum(student['scores']['Math'] for student in class_1)
math_average_1 = math_score_1 / 2
print(math_average_1)

class_2 = school_records['Class_2']['Students']
math_score_2 = sum(student['scores']['Math'] for student in class_2)
math_average_2 = math_score_2 / 2
print(math_average_2)

print((math_average_1 + math_average_2) / 2)
        


