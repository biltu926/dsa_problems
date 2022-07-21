import exceptions
from utility import Utils
from subscription import MusicSubscriptionFactory, PodcastSubscriptionFactory, VideoSubscriptionFactory
from topup import FourDeviceTopupFactory, TenDeviceTopupFactory, get_topup

utils = Utils()

class UserSubscription():

    subscriptions = {}
    topups = {}

    topup = False
    overdue = 0

    def __init__(self) -> None:
        self.start_date: str

    def set_date(self, starting_date):
        try:
            utils.date_validator(starting_date)
        except ValueError:
            self.start_date = None
            raise exceptions.InvalidDate('INVALID_DATE')
        self.start_date = starting_date

    def total_overdue(self):
        for _, subscription in UserSubscription.subscriptions.items():
            UserSubscription.overdue += subscription.renewal_amount()

    def get_overdue_amount(self):
        self.total_overdue()
        if not UserSubscription.subscriptions:
            raise exceptions.SubscriptionNotFound('SUBSCRIPTIONS_NOT_FOUND')
        return  UserSubscription.overdue

    def print_renewal_details(self):
        if not UserSubscription.subscriptions:
            raise exceptions.SubscriptionNotFound('SUBSCRIPTIONS_NOT_FOUND')
        
        for _, subscription in UserSubscription.subscriptions.items():
            print('RENEWAL_REMINDER', subscription.name, subscription.reminder())
        
        print('RENEWAL_AMOUNT', self.get_overdue_amount())
        

    def add_subscription(self, category, plan):
        if category in UserSubscription.subscriptions:
            raise exceptions.DuplicateCategory('ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY')
        
        if not self.start_date:
            raise exceptions.InvalidDate('ADD_SUBSCRIPTION_FAILED INVALID_DATE')

        subscription = None

        if category == 'MUSIC':
            subscription = MusicSubscriptionFactory()._create_subscription(plan, self.start_date)
        elif category == 'VIDEO':
            subscription = VideoSubscriptionFactory()._create_subscription(plan, self.start_date)
        elif category == 'PODCAST':
            subscription = PodcastSubscriptionFactory()._create_subscription(plan, self.start_date)

        if subscription:
            self.subscriptions.update({category: subscription})
    
    def add_topup(self, topup_plan, extention):

        if not self.start_date:
            raise exceptions.InvalidDate('ADD_TOPUP_FAILED INVALID_DATE')
            
        if not UserSubscription.subscriptions:
            raise exceptions.SubscriptionNotFound('ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND')
        
        if UserSubscription.topups:
            raise exceptions.SubscriptionNotFound('ADD_TOPUP_FAILED DUPLICATE_TOPUP')

        topup = get_topup(topup_plan, extention)
        UserSubscription.topups.update({topup.name: topup})
        UserSubscription.topup = True
        UserSubscription.overdue += (topup.price * int(extention))

        for _, subscription in UserSubscription.subscriptions.items():
            subscription.no_of_devices += topup.device_count()
