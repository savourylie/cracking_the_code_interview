def zero_matrix(mat):
	zero_rows = set()
	zero_cols = set()

	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j] == 0:
				zero_rows.add(i)
				zero_cols.add(j)

	return [[mat[i][j] if i not in zero_rows and j not in zero_cols else 0 for j in range(len(mat[0]))] for i in range(len(mat))]


if __name__ == '__main__':
	mat1 = [[1, 2, 0], [1, 1, 0], [1, 1, 1]]
	mat_result1 = [[0, 0, 0], [0, 0, 0], [1, 1, 0]]

	mat2 = [[1, 2, 1], [1, 1, 0], [1, 1, 1]]
	mat_result2 = [[1, 2, 0], [0, 0, 0], [1, 1, 0]]
	
	assert zero_matrix(mat1) == mat_result1
	assert zero_matrix(mat2) == mat_result2
