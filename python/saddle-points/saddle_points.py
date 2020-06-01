from typing import List, Dict


def saddle_points(matrix: List[List]) -> Dict[str, int]:
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError('Error: matrix is not rectangular')
    buf = [{'row': i + 1, 'column': j + 1}
            for i in range(len(matrix))
            for j in range(len(matrix[0]))
            if max(matrix[i]) == matrix[i][j] == min([matrix[k][j] for k in range(len(matrix))])
          ]
    return buf


if __name__ == '__main__':
    print(saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]]))