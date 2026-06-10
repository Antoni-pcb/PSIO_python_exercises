#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Dict, Optional
import copy

class Product:
    def __init__(self, id_: Optional[str], name: str, price: float) -> None:
        if id_ is None:
            self.id = Product.generate_id(name)
        else:
            self.id = id_
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} [{self.id}] : ${self.price:.2f}"
    
    def __eq__(self, other) -> bool:
        if other.id == self.id and other.name == self.name and other.price == self.price:
            return True
        return False
    
    def generate_id(name: str) -> str:
        return f"{name.replace(' ', '')}_{len(name)}"
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        self._price = min(value, 100.)


class Catalogue:
    Inventory = Dict[str, Product]

    def __init__(self, inventory: Inventory = {}) -> None:
        self.inventory = copy.deepcopy(inventory)
    
    def add_product(self, product: Product) -> None:
        self.inventory[product.id] = copy.deepcopy(product)
    
    def __contains__(self, id: str) -> bool:
        return True if id in self.inventory else False
        
