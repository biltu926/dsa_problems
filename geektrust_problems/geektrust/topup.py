from abc import ABC, abstractmethod

class Topup(ABC):
    def __init__(self, extention) -> None:
        super().__init__()
        self.name: str
        self.default_devices: int
        self.price: float
        self.extention_requested: int = extention
        self.default_validity: int

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def device_count(self):
        pass


class FourDeviceTopup(Topup):
    def __init__(self, extention) -> None:
        super().__init__(extention)
        self.name = 'FOUR_DEVICE'
        self.default_devices = 4
        self.default_validity = 1
        self.price = 50
        self.extention_requested = extention

    def cost(self):
        if self.extention_requested <= self.default_validity:
            return 0
        else:
            return self.extention_requested * self.price

    def device_count(self):
        return self.default_devices

class TenDeviceTopup(Topup):
    def __init__(self, extention) -> None:
        super().__init__(extention)
        self.name = 'TEN_DEVICE'
        self.default_devices = 10
        self.default_validity = 1
        self.price = 100
        self.extention_requested = extention

    def cost(self):
        if self.extention_requested <= self.default_validity:
            return 0
        else:
            return self.extention_requested * self.price

    def device_count(self):
        return self.default_devices


class TopupFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def _create_topup(self):
        pass

class FourDeviceTopupFactory(TopupFactory):
    def __init__(self) -> None:
        super().__init__()

    def _create_topup(self, extention):
        return FourDeviceTopup(extention)


class TenDeviceTopupFactory(TopupFactory):
    def __init__(self) -> None:
        super().__init__()

    def _create_topup(self, extention):
        return TenDeviceTopup(extention)

def get_topup(plan, extention):
    if plan == 'FOUR_DEVICE':
        return FourDeviceTopupFactory()._create_topup(extention)
    elif plan == 'TEN_DEVICE':
        return TenDeviceTopupFactory()._create_topup(extention)
    else:
        pass
    return