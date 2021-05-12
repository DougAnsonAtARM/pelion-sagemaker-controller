#!/bin/sh

set -x

python3 -m pip uninstall -y pelion_sagemaker_controller
python3 -m pip install --index-url https://test.pypi.org/simple/ pelion_sagemaker_controller
