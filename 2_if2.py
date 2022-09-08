"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def proof(first_str, second_str):
  if(not(type(first_str) == str and type(second_str) == str)):
    return(0)
  if first_str == second_str:
    return(1)
  if first_str != second_str and len(first_str) > len(second_str):
    return(2)
  if first_str != second_str and second_str == ('learn'):
    return(3)

def main():
  first_str = (1)
  second_str = ('Hi how are you')
  print(proof(first_str,second_str))
  first_str = ('Hi how are you')
  second_str = ('Hi how are you')
  print(proof(first_str,second_str))  
  first_str = ('Hi how are you to')
  second_str = ('Hi how are you')
  print(proof(first_str,second_str))
  first_str = ('Hi')
  second_str = ('learn')
  print(proof(first_str,second_str))

    
if __name__ == "__main__":
  main()
