import numpy as np

class WeakClassifier:
    def __init__(self):
        self.feature_index = None
        self.threshold = None
        self.alpha = None

    def train(self, X, y, weights):
        n_samples, n_features = X.shape
        best_error = float('inf')

        for feature_index in range(n_features):
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                polarity = 1
                predictions = np.ones(n_samples)

                predictions[X[:, feature_index] < threshold] = -1

                error = sum(weights[y != predictions])

                if error < best_error:
                    best_error = error
                    self.feature_index = feature_index
                    self.threshold = threshold
                    self.polarity = polarity

    def predict(self, X):
        n_samples = X.shape[0]
        predictions = np.ones(n_samples)

        if self.polarity == 1:
            predictions[X[:, self.feature_index] < self.threshold] = -1
        else:
            predictions[X[:, self.feature_index] > self.threshold] = -1

        return predictions


class Boosting:
    def __init__(self, n_classifiers=5):
        self.n_classifiers = n_classifiers
        self.classifiers = []

    def train(self, X, y):
        n_samples, _ = X.shape
        weights = np.full(n_samples, 1/n_samples)

        for _ in range(self.n_classifiers):
            classifier = WeakClassifier()
            classifier.train(X, y, weights)
            predictions = classifier.predict(X)
            error = sum(weights[y != predictions])

            alpha = 0.5 * np.log((1 - error) / (error + 1e-10))
            weights *= np.exp(-alpha * y * predictions)
            weights /= np.sum(weights)

            classifier.alpha = alpha
            self.classifiers.append(classifier)

    def predict(self, X):
        n_samples = X.shape[0]
        predictions = np.zeros(n_samples)

        for classifier in self.classifiers:
            predictions += classifier.alpha * classifier.predict(X)

        return np.sign(predictions)


# Ejemplo de uso
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]])
y = np.array([1, 1, 1, -1, -1, -1, 1, 1, 1])

boosting = Boosting(n_classifiers=5)
boosting.train(X, y)

# Predicción de nuevos datos
new_X = np.array([[0, 0], [10, 10]])
predictions = boosting.predict(new_X)
print("Predictions:", predictions)
