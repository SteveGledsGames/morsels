def add(m1, m2):
    added_list = []
    zipped_list = zip(m1, m2)
    print(type(zipped_list))
    for list_item in zipped_list:
        added_list[list_item] = zipped_list[list_item][0]
    return added_list

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
summary_matrix = add(matrix1, matrix2)
for item in summary_matrix:
     print(item)