from .classes import Foreman, ConcreteHouseBuilder


builder = ConcreteHouseBuilder()

foreman = Foreman(builder)
mansion = foreman.build_mansion()
print(
    f"This mansion has {mansion.bedrooms} bedrooms, {mansion.bathrooms} "
    f"bathrooms and {mansion.living_rooms} living room."
)

small_house = foreman.build_small_house()
print(
    f"This small house has {small_house.bedrooms} bedroom and "
    f"{small_house.bathrooms} bathroom."
)
