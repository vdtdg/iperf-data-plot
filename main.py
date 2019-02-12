import json
from pprint import pprint
import matplotlib.pyplot as plt
import talib as ta
import numpy as np
import sys
import argparse


def print_file_info(data):
    pprint(data['start'])
    pprint(data['end'])


def chart(args, data):
    # Setting the default values
    expected_bandwidth = 0
    ema = 60
    if args.protocol == 'udp':
        sum_string = 'sum'
    else:
        sum_string = 'sum_sent'
    if args.ema is not None:
        ema = int(args.ema)
    if args.expectedbw is not None:
        expected_bandwidth = int(args.expectedbw)

    debit = []
    intervals = data['intervals']
    for i in intervals:
        debit.append(i['sum']['bits_per_second'])

    plt.plot(debit, label='Bandwitdh (per second)')

    plt.axhline(data['end'][sum_string]['bits_per_second'], color='r', label='Avg bandwidth')
    plt.axhline(expected_bandwidth * 1000000, color='g', label='Expected bandwidth')
    plt.plot(ta.EMA(np.array(debit), ema), label='Bandwidth {} period moving average'.format(ema))

    plt.title("{}, {}, {:.3}GB file".format(data['start']['timestamp']['time'],
                                         data['start']['test_start']['protocol'],
                                         data['end'][sum_string]['bytes']/1000000000))
    plt.legend()
    plt.ylim(bottom=0)
    plt.ylabel('bit/s')
    plt.xlabel('time interval')
    plt.show()


def main(argv):
    parser = argparse.ArgumentParser(description='Simple python iperf JSON data vizualiser.')
    parser.add_argument('input', nargs='?', help='JSON output file from iperf')
    parser.add_argument('-a', '--ema', help='Exponential moving average used to smooth the bandwidth. Default at 60.', type=int)
    parser.add_argument('-e', '--expectedbw', help='Expected bandwidth to be plotted in Mb.')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
    args = parser.parse_args(argv)
    with open(args.input) as f:
        data = json.load(f)
        if args.verbose:
            print_file_info(data)
        if data['start']['test_start']['protocol'] == 'UDP':
            args.protocol = 'udp'
        else:
            args.protocol = 'tcp'
        chart(args, data)


if __name__ == "__main__":
    main(sys.argv[1:])

# todo : remove ta lib requirement
# todo : test with a tcp output file
# todo : add more info in the print_file_info and to the verbose fonction
