# Autor: Daniel Alejandro Flores Sepulveda
# Programa de Aprendizaje Bayesiano básico

class BayesianLearning:
    def __init__(self, prior_belief):
        self.prior_belief = prior_belief

    def update_belief(self, likelihood):
        # Teorema de Bayes: P(H|E) = P(E|H) * P(H) / P(E)
        # Donde:
        #   P(H|E) es la probabilidad posterior (belief) de H después de observar E
        #   P(E|H) es la verosimilitud de E dada H (likelihood)
        #   P(H) es la probabilidad a priori (prior belief) de H
        #   P(E) es la probabilidad marginal de E (normalización)

        # Normalización (P(E)): Se puede omitir en este caso ya que es constante y no afecta la comparación relativa.
        # Actualización del belief: P(H|E) = P(E|H) * P(H)
        posterior_belief = likelihood * self.prior_belief
        self.prior_belief = posterior_belief
        return posterior_belief

# Datos de ejemplo
prior_belief = 0.3  # Probabilidad a priori de un evento H
likelihood = 0.8    # Verosimilitud de observar un evento E dado que H es verdadero

# Inicialización del proceso de aprendizaje
learner = BayesianLearning(prior_belief)

# Actualización del belief después de observar un nuevo dato
posterior_belief = learner.update_belief(likelihood)

print("Probabilidad a priori:", prior_belief)
print("Verosimilitud:", likelihood)
print("Probabilidad posterior:", posterior_belief)
