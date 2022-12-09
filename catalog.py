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
        pass

    def __len__(self):
        """
        Возвращает количество товара на складе
        """
        pass

