# a3_sdk_py

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
    env='test' # production, test. default: production
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