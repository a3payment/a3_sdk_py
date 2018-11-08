# a3_sdk_py

## Using

Import

```python
import A3SDK
```

Define

```python
a3 = A3SDK(
    'TEST_MERCHANT123',
    '686f1c3c-5dce-11e8-966f-1bf2ed34490d',
    cert_crt='/home/vanzhiganov/Documents/ssl/anzhiganov.crt',
    cert_key='/home/vanzhiganov/Documents/ssl/private.key',
    # production, test. default: production
    # env='test',
    test=True,
    debug=True
)
```

Using

```python
a3.init_payment(
    payment_type='CARD',
    phone='79154747270',
    order_id='101010',
    amount=123.23,
    fee=1.21,
    currency=643,
    format='soap' # soap, json. default: soap
)
```

## Logging

```python
self.logger.warning(
    'Protocol problem: %s',
    'connection reset',
    extra={'clientip': '192.168.0.1', 'user': 'a3loggs'}
)
```

or

```python
self.logger.error('error')
```

```
curl https://sandbox3.payture.com/api/MobilePay?Key=TestMerchant&PayToken=QndiR1VnU1c1RUxNQWtHQTFVRUJoTUNWVk1&OrderId=765274662064352224501405313655251654
```

# Certs

    openssl pkcs12 -in filename.p12 -nocerts -out filename.key

    openssl pkcs12 -in filename.p12 -clcerts -nokeys -out filename.crt 
