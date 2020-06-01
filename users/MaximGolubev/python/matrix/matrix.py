import typing


class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = [
            [int(num) for num in line.split(' ')]
            for line in matrix_string.split('\n')
        ]

    def row(self, idx: int) -> typing.Optional[typing.List]:
        return (self.matrix[idx - 1]
                if self.matrix and 0 < idx <= len(self.matrix)
                else None)

    def column(self, idx: int) -> typing.Optional[typing.List]:
        return ([line[idx - 1] for line in self.matrix]
                if self.matrix and 0 < idx <= len(self.matrix[0])
                else None)


if __name__ == '__main__':
    empty = Matrix('\n\n\n')
    print(empty.row(0), empty.column(0))
