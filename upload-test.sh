#!/bin/bash

echo "Start to build package"
rm -rf ailabs_asr.egg-info/ build/ dist/
python setup.py sdist bdist_wheel

echo "Upload package to testing PyPI"
twine upload --repository-url https://test.pypi.org/legacy/ dist/*