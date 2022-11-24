import pytest
import requests
import json
import logging

def test_login_valid(get_base_url):
    url = get_base_url + '/api/otc/api/v1/quote/'
    headers = {
        'Accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Token': 'USER_TOKEN_LOGIN_ad89165c8f9a3cf052d4dfb92836cf90_461c31f6ab584618baf63587b9ba206c'
    }
    data = {
        'baseCurrency': 'BTC',
        'orderAmountInOrderCurrency': '0',
        'orderCurrency': 'USD',
        'orderSizeInBaseCurrency': '0.01',
        'side': 'BUY'
        }

    resp = requests.post(url, json=data, headers=headers)
    assert resp.status_code == 200, resp.text
    # logging.log(msg=resp)


def test_get_market(get_base_url):
    url = get_base_url + '/api/otc/api/v1/getMarket/'
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }

    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200, resp.text
    logging.getLogger().info(resp)
