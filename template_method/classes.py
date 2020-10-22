from abc import ABC, abstractmethod


class LivingBeing(ABC):
    @abstractmethod
    def be_born(self):  # pragma: no cover
        pass

    @abstractmethod
    def live(self):  # pragma: no cover
        pass

    @abstractmethod
    def die(self):  # pragma: no cover
        pass

    def do_life_cycle(self):
        """This is the template method. Subclasses must implement the
        other three methods.
        """
        self.be_born()
        self.live()
        self.die()


class Turtle(LivingBeing):
    def be_born(self):
        print("A turtle was born.")

    def live(self):
        print("This turtle lives and is 150 years old.")

    def die(self):
        print("The turtle has died.")


class Bee(LivingBeing):
    def be_born(self):
        print("A bee was just born.")

    def live(self):
        print("The bee has been alive for 5 days.")

    def die(self):
        print("Unfortunately, this bee has just died.")
