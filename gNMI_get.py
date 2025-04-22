#!/usr/bin/env python3

from pygnmi.client import gNMIclient
import json
import yaml
import os

if __name__ == '__main__':

    def parse_config(config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config

    app_config = (parse_config('config.yaml'))
    data_dir = "data"
    username = (app_config['defaults']['username'])
    password = (app_config['defaults']['password'])
    grpc_port = (app_config['defaults']['grpc_port'])
    devices = (app_config['devices'])

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    for device in devices:
        host = (device['ipv4'], grpc_port)
        path = (device['paths'])
        with gNMIclient(target=host, username=username, password=password, insecure=True, debug=0) as gc:
            result = gc.get(prefix="cisco_native:", path=path, encoding='json_ietf', datatype='all')
            result["notification"][0]["device"] = device['name']
            with open(data_dir + "/" + device['name'] + '_data.json', 'w') as f:
                json.dump(result, f, indent=4)
