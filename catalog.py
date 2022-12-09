class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, args: dict):
        self.id = args.get('id')
        self.title = args.get('title')
        self.price = args.get('price')
        self.count = args.get('count')
        self.category = args.get('category')

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

