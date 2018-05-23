# coding: utf-8

import re
import requests
from jinja2 import Environment, PackageLoader, select_autoescape
from A3SDK import Exceptions
from A3SDK.base import Base


class SOAPRequests(object):
    def __init__(self):
        self.environment = 'production'
        self.j2_env = Environment(
            loader=PackageLoader('A3SDK', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def build(self, name, **args):
        template = self.j2_env.get_template('{}_request.xml'.format(name))
        return template.render(**args)

    def execute(self, name, **args):
        # print(args['env'])
        headers = {
            'content-type': 'text/xml'
        }

        link = 'https://pfront2.a-3.ru/ProcessingFront/ProcessingFrontWS?WSDL'
        if self.environment == 'test':
            link = 'https://devpfront2.a-3.ru/ProcessingFront/ProcessingFrontWS?WSDL'

        cert_crt = '/home/vanzhiganov/Documents/ssl/anzhiganov.crt'
        cert_key = '/home/vanzhiganov/Documents/ssl/private.key'

        print(requests.get(
            link,
            data=self.build(name, **args),
            headers=headers,
            cert=(
                cert_crt,
                cert_key
            )
        ).text)

        res = requests.post(
            link,
            data=self.build(name, **args),
            headers=headers,
            cert=(
                cert_crt,
                cert_key
            )
        )

        return res.text.encode()


class JSONRequests(object):
    def execite(self, name, **args):
        return


class A3SDK(Base):
    REQUES_METHODS = {
        'soap': SOAPRequests,
        'json': JSONRequests
    }

    def init_payment(self, **args):
        """"""
        # print(1)
        parameters = dict()

        if args.get('payment_type').upper() not in self.PAYMENT_TYPES:
            raise Exceptions.InvalidPaymentType(args.get('payment_type'))
        if not self.validate_phone(args.get('phone')):
            raise Exceptions.InvalidPhoneNumber(args.get('phone'))
        if type(args.get('amount')) not in (float, int):
            raise Exceptions.InvalidAmountType(type(args.get('amount')))
        if type(args.get('fee')) not in (float, int):
            raise Exceptions.InvalidCurrencyType(type(args.get('fee')))
        if type(args.get('currency')) != int:
            raise Exceptions.InvalidCurrencyType(type(args.get('currency')))

        parameters['merchant_id'] = self.merchant_id
        parameters['payment_type'] = args.get('payment_type').upper()
        parameters['phone'] = args.get('phone')
        parameters['amount'] = args.get('amount')
        parameters['fee'] = args.get('fee')
        # TODO: mb validate it?
        parameters['order_id'] = args.get('order_id')

        if parameters['payment_type'] in ['ANDROIDPAY', 'APPLEPAY']:
            if not args.get('token'):
                raise Exceptions.MissingToken()
            parameters['token'] = args.get('token')
        else:
            # TODO: добавить ключ `url_success`
            parameters['url_success'] = args.get('url_success')
            # TODO: добавить ключ `url_fail`
            parameters['url_fail'] = args.get('url_fail')

        # 
        execute = self.REQUES_METHODS[args.get('format', 'soap')]()
        execute.environment = self.env
        
        return execute.execute('init_payment', **parameters)
