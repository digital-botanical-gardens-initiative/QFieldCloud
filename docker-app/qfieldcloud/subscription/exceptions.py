class SubscriptionException(Exception):
    ...


class NotPremiumPlanException(SubscriptionException):
    ...