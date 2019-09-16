# After much work I finally have this working. Next step is to see if I can do it all in one loop
# Then, convert to list comprehensions
def add(m1, m2):
    added_item = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            added_item.append(m1[i][j] + m2[i][j])
    added_list = []
    for i in range(len(m1)):
        new_item = []
        for j in range(len(m1[0])):
            position = (i * len(m1[0]) + j)
            new_item.append(added_item[position])
        # print(new_item)
        added_list.append(new_item)    
    return added_list


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
summary_list = add(matrix1, matrix2)
print(summary_list)
matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
# [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
summary_list = add(matrix1, matrix2)
print(summary_list)
