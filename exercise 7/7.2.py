class SparseMatrix:
    def __init__(self, n_rows, n_cols, data=None):
        self.dims = (n_rows, n_cols)
        self.data = data.copy() if data else {}
        self._validate()
    def _validate(self):
        for (r, c), v in list(self.data.items()):
            if not (0 <= r < self.dims[0] and 0 <= c < self.dims[1]):
                raise IndexError("Indices out of bounds.")
            if v == 0:
                del self.data[(r, c)]
    def __getitem__(self, key):           
        return self.data.get(key, 0.0)
    def __setitem__(self, key, value):
        r, c = key
        if not (0 <= r < self.dims[0] and 0 <= c < self.dims[1]):
            raise IndexError("Indices out of bounds.")
        if value == 0:
            self.data.pop(key, None)
        else:
            self.data[key] = value
    def __repr__(self):
        return f"SparseMatrix(dims={self.dims [0]}x {self.dims[1]}, stored={len (self.data)})"
Matrix = SparseMatrix(1000, 1000)
Matrix[10, 20] = 5.0
Matrix[500, 500] = 3.0
print(Matrix)
print(f"Value at (10, 20): {Matrix[10, 20]}")
print(f"Value at (0, 0): {Matrix[0, 0]}")