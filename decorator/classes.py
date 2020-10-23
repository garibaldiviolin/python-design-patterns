class Algorithm:
    """This algorithm only has a simple sum operation."""
    def __init__(self, *numbers):
        self.numbers = numbers

    def calculate(self):
        result = 0
        for number in self.numbers:
            result += number
        return result


class LoggedAlgorithm:
    """This is the decorator class. It logs (prints) the operations done
    by the Algorithm object.
    """
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def calculate(self):
        print("Calling calculate operation...")
        result = self.algorithm.calculate()
        print(f"The result is {result}.")
        return result
