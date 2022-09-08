"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  while True:
    try:
      how_are_you = input('Как дела? ')
      if how_are_you == 'Хорошо':
        print('Ну вот и славно')
        
    except KeyboardInterrupt:
      print('Пока')
      break
if __name__ == "__main__":
    hello_user()
