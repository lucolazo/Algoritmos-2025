# 6- Leer una palabra y visualizarla en forma inversa.

word = input("Ingrese una palabra: ")

stack_letters = Stack()

for letter in word:
    stack_letters.push(letter)

inverse_word = ''
for i in range(stack_letters.size()):
    inverse_word += stack_letters.pop()

print(inverse_word)