from abc import ABC, abstractmethod
from plan import Plan, PremiumPlanFactory, PersonalPlanFactory, FreePlanfactory
from utility import Utils


utils = Utils()

class Subscription(ABC):
    def __init__(self, start_date, plan: Plan, no_of_devices=1) -> None:
        super().__init__()
        self.name: str
        self.start_date = start_date
        self.plan = plan
        self.no_of_devices = no_of_devices

    def __repr__(self):
        return f'subscription name: {self.name}\n start date: {self.start_date}\n plan: {self.plan}\n \
                number of devices: {self.no_of_devices}\n\n'

    @abstractmethod
    def renewal_amount(self):
        pass

    @abstractmethod
    def expiration(self):
        pass

    @abstractmethod
    def reminder(self):
        pass


class MusicSubscription(Subscription):
    def __init__(self, start_date, plan: Plan) -> None:
        super().__init__(start_date, plan)
        self.name = 'MUSIC'
        self.plan = plan

    def renewal_amount(self):
        return self.plan.get_rate()

    def expiration(self):
        valid_upto_months = self.plan.get_duration()
        expiry_date = utils.calculate_future_date(self.start_date, months_ahead=valid_upto_months)
        return expiry_date

    def reminder(self):
        expiry_date = self.expiration()
        reminder_date = utils.calculate_past_date(expiry_date, days_behind=10)
        return reminder_date


class VideoSubscription(Subscription):
    def __init__(self, start_date, plan: Plan) -> None:
        super().__init__(start_date, plan)
        self.name = 'VIDEO'
        self.plan = plan

    def renewal_amount(self):
        return self.plan.get_rate()

    def expiration(self):
        valid_upto_months = self.plan.get_duration()
        expiry_date = utils.calculate_future_date(self.start_date, months_ahead=valid_upto_months)
        return expiry_date

    def reminder(self):
        expiry_date = self.expiration()
        reminder_date = utils.calculate_past_date(expiry_date, days_behind=10)
        return reminder_date


class PodcastSubscription(Subscription):
    def __init__(self, start_date, plan: Plan) -> None:
        super().__init__(start_date, plan)
        self.name = 'PODCAST'
        self.plan = plan
    
    def renewal_amount(self):
        return self.plan.get_rate()

    def expiration(self):
        valid_upto_months = self.plan.get_duration()
        expiry_date = utils.calculate_future_date(self.start_date, months_ahead=valid_upto_months)
        return expiry_date

    def reminder(self):
        expiry_date = self.expiration()
        reminder_date = utils.calculate_past_date(expiry_date, days_behind=10)
        return reminder_date


class SubscriptionFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def _create_subscription():
        pass


class MusicSubscriptionFactory(SubscriptionFactory):
    def __init__(self) -> None:
        super().__init__()

    def _create_subscription(self, plan_name, start_date):
        if plan_name == 'PREMIUM':
            plan = PremiumPlanFactory()._create_plan(3, 250)
        elif plan_name == 'PERSONAL':
            plan = PersonalPlanFactory()._create_plan(1, 100)
        elif plan_name == 'FREE':
            plan = FreePlanfactory()._create_plan(1, 0)
        else:
            pass
        return MusicSubscription(start_date, plan)


class VideoSubscriptionFactory(SubscriptionFactory):
    def __init__(self) -> None:
        super().__init__()

    def _create_subscription(self, plan_name, start_date):
        if plan_name == 'PREMIUM':
            plan = PremiumPlanFactory()._create_plan(3, 500)
        elif plan_name == 'PERSONAL':
            plan = PersonalPlanFactory()._create_plan(1, 200)
        elif plan_name == 'FREE':
            plan = FreePlanfactory()._create_plan(1, 0)
        else:
            pass
        return VideoSubscription(start_date, plan)


class PodcastSubscriptionFactory(SubscriptionFactory):
    def __init__(self) -> None:
        super().__init__()

    def _create_subscription(self, plan_name, start_date):
        if plan_name == 'PREMIUM':
            plan = PremiumPlanFactory()._create_plan(3, 300)
        elif plan_name == 'PERSONAL':
            plan = PersonalPlanFactory()._create_plan(1, 100)
        elif plan_name == 'FREE':
            plan = FreePlanfactory()._create_plan(1, 0)
        else:
            pass
        return PodcastSubscription(start_date, plan)

    