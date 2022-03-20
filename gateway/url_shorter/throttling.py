from rest_framework.throttling import UserRateThrottle


class LimitUserRequests(UserRateThrottle):
    rate = '100/minute'
