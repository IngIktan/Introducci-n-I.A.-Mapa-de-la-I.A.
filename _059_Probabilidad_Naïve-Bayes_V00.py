# Autor: Daniel Alejandro Flores Sepulveda
# Programa de ejemplo de clasificación usando Naïve-Bayes

class NaiveBayesClassifier:
    def __init__(self):
        self.class_probs = {}
        self.feature_probs = {}

    def train(self, X, y):
        # Calcula la probabilidad a priori de cada clase
        total_samples = len(y)
        unique_classes = set(y)
        for cls in unique_classes:
            self.class_probs[cls] = sum(1 for label in y if label == cls) / total_samples

        # Calcula la probabilidad condicional de cada característica para cada clase
        for cls in unique_classes:
            cls_samples = [X[i] for i, label in enumerate(y) if label == cls]
            for i in range(len(X[0])):
                feature_values = [sample[i] for sample in cls_samples]
                unique_values = set(feature_values)
                for value in unique_values:
                    feature_count = sum(1 for val in feature_values if val == value)
                    self.feature_probs[(i, value, cls)] = feature_count / len(cls_samples)

    def predict(self, sample):
        # Calcula la probabilidad de cada clase para la muestra dada
        class_scores = {}
        for cls in self.class_probs:
            class_score = self.class_probs[cls]
            for i, value in enumerate(sample):
                if (i, value, cls) in self.feature_probs:
                    class_score *= self.feature_probs[(i, value, cls)]
            class_scores[cls] = class_score

        # Devuelve la clase con la probabilidad más alta
        return max(class_scores, key=class_scores.get)

# Ejemplo de uso
X_train = [[1, 'S'], [1, 'M'], [1, 'M'], [1, 'S'], [1, 'S'],
           [2, 'S'], [2, 'M'], [2, 'M'], [2, 'L'], [2, 'L'],
           [3, 'L'], [3, 'M'], [3, 'M'], [3, 'L'], [3, 'L']]
y_train = ['N', 'N', 'Y', 'Y', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N']

X_test = [2, 'S']

# Entrenamiento
classifier = NaiveBayesClassifier()
classifier.train(X_train, y_train)

# Predicción
prediction = classifier.predict(X_test)
print("Predicción:", prediction)
