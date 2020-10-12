from .classes import Human, CarMaintenance, CodeDevelopment


mechanic = Human(CarMaintenance())
mechanic.talk()
mechanic.work()

developer = Human(CodeDevelopment())
mechanic.talk()
developer.work()
