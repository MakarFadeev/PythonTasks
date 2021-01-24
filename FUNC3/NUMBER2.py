numbers = [1, 2, 3, 4, 5]
def rotateSAndSItem(sequence):
    sequence = [*sequence[2:], *sequence[:2]]
    return sequence
print(rotateSAndSItem(numbers))
