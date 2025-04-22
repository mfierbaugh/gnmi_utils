#!/usr/bin/env python3


import grpc, json, yaml, argparse, logging
from pygnmi.client import gNMIclient, telemetryParser


parser = argparse.ArgumentParser(description='get_alarms.py: retrieve operational data and output to host.xml file')
parser.add_argument('-d','--device', help='Device Hostname',required=True)
parser.add_argument('-u','--username',help='Device Username', required=True)
parser.add_argument('-p','--password',help='Device Password', required=True)
parser.add_argument('-P','--port',default=57400, help='gRPC port default is 57400')
parser.add_argument('-f','--filter',help='xpath filter', required=True)
args = parser.parse_args()


def telemetry_sub(ip, port, username, password, subscribe):
    try:
        with gNMIclient(target=(ip, port), username=username, password=password, insecure=True) as gc:
            telemetry_pull = gc.subscribe2(subscribe=subscribe)
            for telemetry_entry in telemetry_pull:
                print(json.dumps(telemetry_entry, indent=4))

    except grpc.FutureTimeoutError as e:
        print('Failed connecting to', ip, e)

    except ValueError as e:
        print(e)
        pass


def main():
    username = args.username
    password = args.password
    device = args.device
    grpc_port = args.port
    device = args.device

    subscribe={}
    keys=['subscription']
    for key in keys:
        subscribe[key] = []
        item = {'path': args.filter, 'mode': 'ON_CHANGE'}
        subscribe[key].append(item)
    item2 = {"use_aliases": False, 'mode': 'stream', 'encoding': 'json'}
    subscribe.update(item2)

    telemetry_sub(device, grpc_port, username, password, subscribe)


if __name__ == '__main__':
    main()