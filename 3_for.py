"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def count_product_sum(phone_items_sold):
  items_sold_sum = 0
  for sum in phone_items_sold:
    items_sold_sum += sum
  return items_sold_sum

def count_product_avg(phone_items_sold):
  items_sold_sum = 0
  for sum in phone_items_sold:
    items_sold_sum += sum
  return items_sold_sum / len(phone_items_sold)




def main():
  all_phone = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]   

  all_product_sum =0
  all_product_avg =0
  for one_product in all_phone:
    product_sum = count_product_sum(one_product['items_sold'])
    all_product_sum += product_sum
    print(f'Суммарное количество продаж {one_product["product"]}: {product_sum}')
  print(f'Суммарное количество продаж всех товаров: {all_product_sum}')
  for one_product in all_phone:
    product_avg = count_product_avg(one_product['items_sold'])
    all_product_avg += product_avg / len(all_phone)
    print(f'Среднее количество продаж {one_product["product"]}: {product_avg}')
  print(f'Среднее количество продаж всех товаров: {all_product_avg}')
  

if __name__ == "__main__":
    main()
