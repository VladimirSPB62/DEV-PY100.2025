# Объявляем функцию для поиска индекса товара.
def search_index_product(products, product):
    if product in products:
        return products.index(product)
    else:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_index_product(items_list, find_item) # Вызываем функцию, чтобы получить индекс товара.
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
