
def exam(limit, *marks):
    niceExam = 0
    for i in marks:
        if i >= limit:
            niceExam += 1
    whatToReturn = 'Экзамен сдали ' + str(niceExam) + ' учеников'
    return whatToReturn
print(exam(3, 2, 4, 1, 3, 5, 2, 3, 4, 5, 1))
