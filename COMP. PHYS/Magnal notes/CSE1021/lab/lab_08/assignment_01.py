students_enrolled_in_python = {'Alice', 'Bob', 'Charlie', 'David', 'Eva'}
students_enrolled_in_java = {'Charlie', 'David', 'Fiona', 'George', 'Henry'}

#1.Enrolled in both
intersection = students_enrolled_in_python.intersection(students_enrolled_in_java)
print(intersection)

#2.Enrolled in either python or java but not both
symmetric_difference = students_enrolled_in_python.symmetric_difference(students_enrolled_in_java)
print("Students who are enrolled in either Python or Java but not both. : ", symmetric_difference)


#3.Total no of Unique Students
union = students_enrolled_in_python.union(students_enrolled_in_java)
print("Total unique students : ", len(union))

   