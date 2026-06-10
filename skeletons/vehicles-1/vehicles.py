#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TypeVar, Container

class Movable:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

class Vehicle(ABC, Movable):
    def __init__(self, id_: str, brand: str, x: float = 0., y: float = 0.) -> None:
        Movable.__init__(x, y)
        self.id = id_
        self.brand = brand
    
    @abstractmethod
    def max_speed(self) -> float:
        pass

    def __str__(self):
        return f"{self.id} :  {self.brand}"
    

class Car(Vehicle):
    def __init__(self, id_: str, brand: str, engine_hp: float) -> None:
        super().__init__(id_, brand)
        self.engine_hp = engine_hp
    
    def max_speed(self) -> float:
        return self.engine_hp
    

class Bicycle(Vehicle):
    def __init__(self, id_: str, brand: str, n_gears: int) -> None:
        super().__init__(id_, brand)
        self.n_gears = n_gears
    
    def max_speed(self) -> float:
        return 3. * self.n_gears


Veh = TypeVar("Veh", bound = Vehicle)

def vehicle_collection_as_string(container: Container[Veh]) -> str:
    output = ''
    for (i, v) in enumerate(container):
        if i == len(container) - 1:
            output += str(v)
        else:
            output += (str(v) + '\n')
    return output

def compute_min_travel_duration(distance: float, vehicle: Veh) -> float:
    return distance / vehicle.max_speed()

def compute_min_travel_duration_as_string(distance: float, vehicle: Veh) -> str:
    return f"{compute_min_travel_duration(distance, vehicle):.3f} h"