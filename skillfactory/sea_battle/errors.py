class ErrorAddShip(Exception):

    def __init__(self):
        super().__init__("Корабль не может быть расположен в этом месте!!")


class ErrorBuildBoard(Exception):

    def __init__(self):
        super().__init__("Ошибка создания игровой доски!!!")


class ErrorOutOfBoard(Exception):

    def __init__(self):
        super().__init__("Вы не попали в мишень!!!")


class ErrorShot(Exception):
    def __init__(self):
        super().__init__("Вы туда уже стреляли!!!")