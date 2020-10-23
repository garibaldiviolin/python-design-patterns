from .classes import Algorithm, LoggedAlgorithm


algorithm = Algorithm(1, 2, 3)
result = algorithm.calculate()
print(f"{result=}")

logged_algorithm = LoggedAlgorithm(algorithm)
result = logged_algorithm.calculate()
print(f"{result=}")
