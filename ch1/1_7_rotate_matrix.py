def rotate_matrix(mat):
	mat = diag_swap(mat)
	mat = horizontal_swap(mat)

	return mat

def diag_swap(mat):
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if j > i:
				mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

	return mat

def horizontal_swap(mat):
	for i in range(len(mat)):
		for j in range(len(mat[0]) // 2):
			mat[i][j], mat[i][len(mat[0]) - j - 1] = mat[i][len(mat[0]) - j - 1], mat[i][j]

	return mat


if __name__ == '__main__':
	mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
	mat_result1 = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

	mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	mat_result2 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

	assert rotate_matrix(mat2) == mat_result2