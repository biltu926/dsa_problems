
class Base(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class SubscriptionNotFound(Base):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class DuplicateCategory(Base):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class DuplicateTopup(Base):
    def __init__(self, *args) -> None:
        super().__init__(*args)



class InvalidDate(Base):
    def __init__(self, *args) -> None:
        super().__init__(*args)

