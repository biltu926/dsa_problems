import sys
from exceptions import *
from user_subscription import UserSubscription


def main():
    input_file_path = sys.argv[1]
    content = ''
    with open(input_file_path, 'r') as fp:
        content = fp.read()

    command_list = content.split('\n')
    user_subscription = UserSubscription()

    for command in command_list:
        command = command.split(' ')

        try:
            instruction = command[0]

            if instruction == 'START_SUBSCRIPTION':
                start_date = command[1]
                user_subscription.set_date(start_date)

            elif instruction == 'ADD_SUBSCRIPTION':
                category, plan_name = command[1], command[2]
                user_subscription.add_subscription(category, plan_name)

            elif instruction == 'ADD_TOPUP':
                plan_name, extention = command[1], command[2]
                user_subscription.add_topup(plan_name, extention)

            elif instruction == 'PRINT_RENEWAL_DETAILS':
                user_subscription.print_renewal_details()
        

        except (DuplicateTopup, DuplicateCategory, SubscriptionNotFound, InvalidDate) as e:
            print(e)

if __name__ == "__main__":
    main()
