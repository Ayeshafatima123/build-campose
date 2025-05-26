class Beverage:
    def get_description(self):
        return "Unknown Beverage"
    
    def cost(self):
        return 0.0

class Espresso(Beverage):
    def get_description(self):
        return "Espresso"

    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def get_description(self):
        return "House Blend Coffee"

    def cost(self):
        return 0.89

class CondimentDecorator(Beverage):
    def get_description(self):
        raise NotImplementedError

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20

class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return self.beverage.cost() + 0.10

order = Espresso()
print(order.get_description(), "$", order.cost())

order2 = HouseBlend()
order2 = Mocha(order2)
order2 = Whip(order2)
print(order2.get_description(), "$", order2.cost())
