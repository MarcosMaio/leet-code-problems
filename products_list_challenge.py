# Criar uma função que filtra uma lista de dicionarios de produtos, os inputs serão a lista de dicionarios de produtos, o valor maximo, e o valor minimo, a função deve retornar uma lista com os produtos que estão dentro desse intervalo de preço.

list_prod = {
    "Café": 12.50,
    "Chá Verde": 8.75,
    "Chocolate": 15.20,
    "Leite": 6.00,
    "Biscoitos": 10.30,
    "Iogurte": 7.45,
    "Arroz": 20.00,
    "Feijão": 12.90,
    "Azeite de Oliva": 25.50,
    "Macarrão": 5.80
}


def filter_products(list_prod, min, max):
  filter_prod = []
  for prod, price in list_prod.items():
      if min < price < max:
        filter_prod.append(prod)
  print(filter_prod)
  # return filter_prod


# def filter_products(list_prod, min_price, max_price):
#     return [prod for prod, price in list_prod.items() if min_price < price < max_price]

  
filter_products(list_prod, 8.00, 15.00)



