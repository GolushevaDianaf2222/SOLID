from enum import Enum
from abc import ABCMeta, abstractmethod

class Discount():
    @abstractmethod
    def get_discounted_price(self):
         pass

class DiscountFruits(Discount):
     def __init__(self, cost):
         self.cost = cost

         def get_discounted_price(self):
              return self.cost - (self.cost * 0,10)

class DiscountVegetables(Discount):
     def __init__(self, cost):
         self.cost = cost

         def get_discounted_price(self):
              return self.cost - (self.cost * 0,15)

class DiscountCalculator(Discount):
     def __init__(self, cost):
         self.cost = cost
         
         def get_discounted_price(self):
              return self.cost - (self.cost * 0,25)

dc_Fruits =DiscountFruits(100)
print(dc_Fruits.get_discounted_price())

dc_Vegetables = DiscountVegetables(100)
print(dc_Vegetables.get_discounted_price())

dc_Calculator = DiscountCalculator(100)
print(dc_Calculator.get_discounted_price())
