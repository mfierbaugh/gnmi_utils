# Simple example utilities in python for working with gNMI

There are two utilities in this repo to provide examples of using pyGNMI to both get values via gRPC and to subscribe to "on change" telemetry. 

    gNMI_get.py

This utility reads the config yaml and loops through the paths for each device using the get function. 

    usage: subscribe.py [-h] -d DEVICE -u USERNAME -p PASSWORD [-P PORT] -f FILTER

This utility takes command line arguments to specifiy the values:

example: 
    ./subscribe.py -d 198.18.200.10 -u admin -p cisco123 -f openconfig-system:system/alarms  

