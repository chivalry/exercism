export class Matrix {
    constructor(matrix_string) {
        this.matrix = matrix_string;
    }

    get rows() {
        if (this._rows) return this._rows;
        this._rows = this.matrix.split('\n').map((row) => {
            return row.split(' ').map((elem) => Number(elem))
        });
        return this._rows;
    }

    get columns() {
        if (this._cols) return this._cols;
        this._cols = this.rows[0].map((col) => []);
        this.rows.forEach((row) => {
            row.forEach((elem, index) => this._cols[index].push(elem));
        });
        return this._cols;
    }
}
