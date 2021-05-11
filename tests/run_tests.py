# General OS
import os
import sys
import uuid
import signal
import json
import base64 
import struct
import argparse

# Logging
import logging

NAME='seatpapi'

# Sagemaker Edge Agent To Pelion API (seatpapi)
import seatpapi as pelion

# Create logger
logger = logging.getLogger(NAME)

# Signal handler to exit the service...
def exit_signal(signum, frame):
    logger.info(NAME + ": Closing down on signal: {signum}".format(signum=signum))
    sys.exit(0)
    
# Run Tests
def run_tests(api_key,device_id,endpoint_api):
    # Allocate
    api = pelion.PelionAPI(api_key,device_id,endpoint_api)
    
    # List Models
    json = api.pelion_list_models()
    print('Model List: ' + str(json))

    # Get Last Results
    json = api.pelion_last_cmd_result()
    print('Last command result: ' + str(json))
    
    # Get Configuration
    json = api.pelion_get_config()
    print('Configuration: ' + str(json))
    
# Main    
def main():
    # Initialize signals
    signal.signal(signal.SIGTERM, exit_signal)
    
    # Initialize logging level
    logging.basicConfig(level=logging.INFO, filemode='w', format='[%(levelname)s] %(name)s - %(message)s')

    # Parse any arguments we have passed
    parser = argparse.ArgumentParser(
        description='Test harness for seatpapi',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-a', '--api_key', dest="api_key", help='Pelion Application Key', type=str, default="ak_xxxx")
    parser.add_argument('-d', '--device_id', dest="device_id", help='Pelion Gateway Device ID', type=str, default="012345")
    parser.add_argument('-e', '--endpoint_api', dest="endpoint_api", help='Pelion API Endpoint', type=str, default="api.us-east-1.mbedcloud.com")
    args = parser.parse_args()
    
    # Run Tests
    run_tests(args.api_key,args.device_id,args.endpoint_api)    

if __name__ == "__main__":
    main()