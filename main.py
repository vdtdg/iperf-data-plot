import json
from pprint import pprint
import matplotlib.pyplot as plt
import talib as ta
import numpy as np


def print_file_info(data):
    pprint(data['start'])
    pprint(data['end'])


def tcp_chart(data):
    debit = []
    intervals = data['intervals']
    for i in intervals:
        debit.append(i['sum']['bits_per_second'])

    plt.plot(debit, label='bandwitdh per second')
    plt.axhline(data['end']['sum_sent']['bits_per_second'], color='r', label='Avg bandwidth')
    plt.title("{}, {}, 1GB file".format(data['start']['timestamp']['time'], data['start']['test_start']['protocol']))
    plt.legend()
    plt.show()


def udp_chart(data):
    debit = []
    intervals = data['intervals']
    for i in intervals:
        debit.append(i['sum']['bits_per_second'])

    plt.plot(debit, label='bandwitdh per second')
    plt.axhline(data['end']['sum']['bits_per_second'], color='r', label='Avg bandwidth')
    plt.plot(ta.EMA(np.array(debit), 60), label='bandwitch 60 period moving average')

    plt.title("{}, {}, 1GB file".format(data['start']['timestamp']['time'], data['start']['test_start']['protocol']))
    plt.legend()
    plt.show()


with open('output.json') as f:
    data = json.load(f)
    print_file_info(data)
    udp_chart(data)
