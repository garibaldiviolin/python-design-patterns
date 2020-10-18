from .classes import ConcreteVehicleFactory1, ConcreteVehicleFactory2


ferrari = ConcreteVehicleFactory1.create_car()
ferrari.run()

airbus_a380 = ConcreteVehicleFactory1.create_aircraft()
airbus_a380.fly()

lamborghini = ConcreteVehicleFactory2.create_car()
lamborghini.run()

boeing_747 = ConcreteVehicleFactory2.create_aircraft()
boeing_747.fly()
