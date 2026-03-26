import numpy as np

class DataScalar:
    def _init_(self):
        self.mean=None
        self.std_dev = None

    def fit(self, data):
        self.mean = np.mean(data)
        self.std_dev = np.std(data)
    def transform(self, data):
        if self.mean is None or self.std_dev is None:
            raise Exception("DataScalar not fitted yet.")
        return (data - self.mean) / self.std_dev
    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)
raw_data = np.array([10, 20, 30, 40, 50])
scaler = DataScalar()
scaled_data = scaler.fit_transform(raw_data)
print (f"Original data: {raw_data}")
print (f"Scaled data: {scaled_data}")
