class Stack:

    elements = []
    #__elements para hacer la variable privada.

    def mostrar_elementos(self):   #Self hace referencia al objeto
        print(self.elements)

#Self.__elements. ".__" para hacer el atributo privado.

stack = Stack()

stack.mostrar_elementos()

from typing import Any, Optional
from random import randint


class Stack:

    def __init__(self):   #Constructor
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:

        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
            )

    def show(self):
        print(self.__elements)

stack = Stack()


for i in range(5):
    stack.push(randint(1, 100))

stack.show()
print(stack.on_top())
stack.show()


from random import randint

from stack import Stack

number_stack = Stack()
even_stack = Stack() #Par
odds_stack = Stack() #Impares

for i in range(10):
    rand_number = randint(1, 100)
    print(rand_number)
    number_stack.push(rand_number)

for i in range(number_stack.size()):
    number = number_stack.pop()
    if number % 2 == 0:
        even_stack.push(number)
    else:
        odds_stack.push(number)