def get_grades(names, j_scores, py_scores, ds_scores, dt_scores):

	largest_j, smallest_j = j_scores[0], j_scores[0]
	largest_py, smallest_py = py_scores[0], py_scores[0]
	largest_ds, smallest_ds = ds_scores[0], ds_scores[0]
	largest_dt, smallest_dt = dt_scores[0], dt_scores[0]

	for score in j_scores:

		if score > largest_j: largest_j = score
		elif score < smallest_j: smallest_j = score

	java_l_index = j_scores.index(largest_j)
	java_s_index = j_scores.index(smallest_j)

	for score in py_scores:

		if score > largest_py: largest_py = score
		elif score < smallest_py: smallest_py = score

	python_l_index = py_scores.index(largest_py)
	python_s_index = py_scores.index(smallest_py)

	for score in ds_scores:

		if score > largest_ds: largest_ds = score
		elif score < smallest_ds: smallest_ds = score

	ds_l_index = ds_scores.index(largest_ds)
	ds_s_index = ds_scores.index(smallest_ds)

	for score in dt_scores:

		if score > largest_dt: largest_dt = score
		elif score < smallest_dt: smallest_dt = score

	dt_l_index = dt_scores.index(largest_dt)
	dt_s_index = dt_scores.index(smallest_dt)


	yield "\n\nName\tJv\tPy\tDS\tDT"

	for index in range (0, len(names)):

		yield f"\n{names[index]}\t{j_scores[index]}\t{py_scores[index]}\t{ds_scores[index]}\t{dt_scores[index]}"


	yield f"""


Highest Java Score: {largest_j} | Student: {names[java_l_index]}
Lowest Java Score: {smallest_j} | Student: {names[java_s_index]}

Highest Python Score: {largest_py} | Student: {names[python_l_index]}
Lowest Python Score: {smallest_py} | Student: {names[python_s_index]}

Highest Data Science Score: {largest_ds} | Student: {names[ds_l_index]}
Lowest Data Science Score: {smallest_ds} | Student: {names[ds_s_index]}

Highest Design Thinking Score: {largest_dt} | Student: {names[dt_l_index]}
Lowest Design Thinking Score: {smallest_dt} | Student: {names[dt_s_index]}

		"""		







count = 0
names = []
j_scores = []
py_scores = []
ds_scores = []
dt_scores = []

students = int(input("Input number of students: "))

while count < students:
	name = input(f"Enter student {count + 1}'s name: ")
	names.append(name)
	count += 1

count = 0
while count < students:
	j_score = int(input(f"Enter student {count + 1}'s Java score: "))
	if j_score < 100 and j_score > 0:
		j_scores.append(j_score)
		count += 1

count = 0
while count < students:
	py_score = int(input(f"Enter student {count + 1}'s Python score: "))
	if py_score < 100 and py_score > 0:
		py_scores.append(py_score)
		count += 1

count = 0
while count < students:
	ds_score = int(input(f"Enter student {count + 1}'s Data Science score: "))
	if ds_score < 100 and ds_score > 0:
		ds_scores.append(ds_score)
		count += 1

count = 0
while count < students:
	dt_score = int(input(f"Enter student {count + 1}'s Design Thinking score: "))
	if dt_score < 100 and dt_score > 0:
		dt_scores.append(dt_score)
		count += 1

result = get_grades(names, j_scores, py_scores, ds_scores, dt_scores)


for count in range(students + 2):

	print(next(result))






