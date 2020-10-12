class Human:
    def __init__(self, activity):
        self._activity = activity

    def talk(self):
        print("Talking...")

    def work(self):
        self._activity.do()


class CodeDevelopment:
    def do(self):
        print("Developing some code...")


class CarMaintenance:
    def do(self):
        print("Repairing the car...")
