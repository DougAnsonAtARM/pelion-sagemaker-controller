#!/bin/sh

rm -rf build dist seatpapi/*info
python3 setup.py sdist bdist_wheel
echo "python3 -m twine upload --repository testpypi dist/*"
echo "python3 -m twine upload --repository pypi dist/*"
