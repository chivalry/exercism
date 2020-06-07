export class Matrix {
    constructor(matrix_string) {
        this._rows = [];
        matrix_string.split('\n').forEach((row) => {
            this._rows.push(row.split(' ').map((elem) => Number(elem)));
        })
        this._cols = [];
        this._rows[0].forEach((col) => this._cols.push([]));
        this._rows.forEach((row) => {
            row.forEach((elem, index) => this._cols[index].push(elem));
        });
    }

    get rows() {
        return this._rows;
    }

    get columns() {
        return this._cols;
    }
}
