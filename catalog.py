class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, *args, **kwargs):
        pass

    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """
        if self.count > 0:
            print(f'товар есть в наличии ({self.count} шт.)')
            return True
        else:
            print('товара нет в наличии')
            return False
    def __len__(self):
        """
        Возвращает количество товара на складе
        """
        pass

