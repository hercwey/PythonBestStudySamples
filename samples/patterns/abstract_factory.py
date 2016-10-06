#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/6 11:58
# @Author  : Hercwey
# @Site    : 
# @File    : abstract_factory.py.py
# @Software: PyCharm

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
# 中文解释：http://blog.csdn.net/zhengzhb/article/details/7359385/

"""Implementation of the abstract factory pattern"""

import random


class PetShop:
    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))


# Stuff that our factory makes

class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()


# Show pets with various factories
if __name__ == "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)

        ### OUTPUT ###
        # We have a lovely Dog
        # It says woof
        # We also have dog food
        # ====================
        # We have a lovely Dog
        # It says woof
        # We also have dog food
        # ====================
        # We have a lovely Cat
        # It says meow
        # We also have cat food
        # ====================
"""
一句话解释：宠物玩具店工厂（就是这里的抽象工厂）包括猫工厂与狗工厂等等
适用场景：
当需要创建的对象是一系列相互关联或相互依赖的产品族时，便可以使用抽象工厂模式。说的更明白一点，就是一个继承体系中，
如果存在着多个等级结构（即存在着多个抽象类），并且分属各个等级结构中的实现类之间存在着一定的关联或者约束，
就可以使用抽象工厂模式。假如各个等级结构中的实现类之间不存在关联或约束，则使用多个独立的工厂来对产品进行创建，则更合适一点。
在使用工厂模式时，只需要关心降低耦合度的目的是否达到了。
"""