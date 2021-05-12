#!/bin/sh

python3 -m pip uninstall -y pelion_sagemaker_controller
echo "python3 -m pip install pelion_sagemaker_controller"
echo "python3 -m pip install --index-url https://test.pypi.org/simple/ pelion_sagemaker_controller"
