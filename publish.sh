#!/bin/sh

rm -rf build dist pelion_sagemaker_controller/*info *info pelion_sagemaker_controller/__*cache*__
python3 setup.py sdist bdist_wheel
echo "python3 -m twine upload --repository testpypi dist/*"
echo "python3 -m twine upload --repository pypi dist/*"
