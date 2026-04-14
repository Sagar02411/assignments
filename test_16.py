Query = """WITH MoreThanAverage AS (
Select student.id
FROM STUDENTS
WHERE marks>AVG(marks)
)"""
PERFORM = """SELECT * FROM MoreThanAverage;"""