from abc import ABC, abstractmethod


class Plan(ABC):
    def __init__(self, duration, rate) -> None:
        super().__init__()
        self.name = ''
        self.duration = duration
        self.rate = rate

    def __repr__(self):
        return f' Plan name: {self.name}\n Plan duration: {self.duration}\n Plan charge: {self.rate}'

    @abstractmethod 
    def get_rate(self):
        return

    @abstractmethod
    def get_duration(self):
        return



class FreePlan(Plan):
    def __init__(self, duration, rate) -> None:
        super().__init__(duration, rate)
        self.name = 'Free Plan'
        self.duration = 1
        self.rate = 0

    def get_rate(self):
        return self.rate
        
    def get_duration(self):
        return self.duration


class PersonalPlan(Plan):
    def __init__(self, duration, rate) -> None:
        super().__init__(duration, rate)
        self.name = 'Personal Plan'
        self.duration = duration
        self.rate = rate

    def get_rate(self):
        return self.rate
        
    def get_duration(self):
        return self.duration


class PremiumPlan(Plan):
    def __init__(self, duration, rate) -> None:
        super().__init__(duration, rate)
        self.name = 'Personal Plan'
        self.duration = duration
        self.rate = rate

    def get_rate(self):
        return self.rate
        
    def get_duration(self):
        return self.duration


class PlanFactory(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def _create_plan(self, duration, rate):
        pass

class PersonalPlanFactory(PlanFactory):
    def __init__(self) -> None:
        super().__init__()

    def _create_plan(self, duration, rate):
        return PersonalPlan(duration, rate)

class PremiumPlanFactory(PlanFactory):
    def __init__(self) -> None:
        super().__init__()
    
    def _create_plan(self, duration, rate):
        return PremiumPlan(duration, rate)


class FreePlanfactory(PlanFactory):
    def __init__(self) -> None:
        super().__init__()

    def _create_plan(self, duration, rate):
        return PremiumPlan(duration, rate)
