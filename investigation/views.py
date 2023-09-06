from django.shortcuts import render
from django.http import HttpResponse
from .Coins import dogecoin, bitcoin, ether, tether, monero, dash
import requests
import json
# import logging


def index(request):
    return render(request, "investigation/index.html")

# key = "0xce0babc8398144aa98d9210d595e3a9714910748" #valid ether
# key = "DBKsPhXJ2A4cK8Z8F8nFbkVpeskYLoNNTk" #valid dogecoin
# key = "XcFLaufF75pyRbAZxgT7A1Vu7GG1qhzDvK" #valid dash
# key = "3EQ8FhqRR2H4Ffd2JsoT8R899B2omscgcX" #valid bitcoin


def publicKeyCheck(request):
    if request.method == 'POST':
        key = request.POST['key']
    if (bitcoin.is_valid_bitcoin_address(key)):

        response_API = requests.get(
            f'https://blockchain.info/balance?active={key}')
        # print(response_API.status_code)
        data = response_API.text
        parse_json = json.loads(data)
        return render(request, "investigation/index.html", {
            "key": key,
            "data": data,
            "message": "valid bitcoin"
        })
    elif ether.is_valid_ethereum_address(key):
        return render(request, "investigation/index.html", {
            "key": key,
            "message": "valid ethereum"
        })
    elif tether.is_valid_tether_address(key):
        return render(request, "investigation/index.html", {
            "key": key,
            "message": "valid tether"
        })
    elif monero.is_valid_monero_address(key):
        return render(request, "investigation/index.html", {
            "key": key,
            "message": "valid monero"
        })
    elif dash.is_valid_dash_address(key):
        return render(request, "investigation/index.html", {
            "key": key,
            "message": "valid dash"
        })
    elif dogecoin.is_valid_dogecoin_address(key):
        return render(request, "investigation/index.html", {
            "key": key,
            "message": "valid dogecoin"
        })
    else:
        return render(request, "investigation/index.html", {
            "key": key,
            "message": "not a valid cryptocurrency"
        })
