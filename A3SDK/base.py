import re


class Base(object):
    PAYMENT_TYPES = ['CARD', 'PHONE', 'ANDROIDPAY', 'APPLEPAY']

    def __init__(self, merchant_id, secret='', **args):
        self.merchant_id = merchant_id
        self.secret = secret
        self.env = 'production' if args.get('env') == 'production' else 'test'

    def validate_phone(self, phone):
        """Validate phone number

        See also: https://en.wikipedia.org/wiki/Telephone_numbers_in_Russia

        >>> Base().validate_phone('9154747270')
        True
        >>> Base().validate_phone('+79154747270')
        True
        >>> Base().validate_phone('89154747270')
        True

        :param phone: str
        :return: bool
        """
        pattern = r"^(\+?7|8)?(9\d{2})(\d{7})$"
        return True if re.compile(pattern).match(phone.replace(' ', '')) else False