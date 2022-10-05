from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
  readme = readme_file.read()

setup(
  name='ailabs-asr',
  version='0.0.11',
  author='Hendryboyz',
  author_email="Hendry.js1247@gmail.com",
  description="Package to utilize the speech to text API powered by AILabs.tw",
  long_description=readme,
  long_description_content_type="text/markdown",
  url="https://github.com/TaiwanAILabs-Yating/asr-python-sdk",
  packages=find_packages(),
  include_package_data=True,
  package_data={'ailabs_asr': ['configs/*.yaml']},
  install_requires=[
    'PyYAML>=6.0',
    'requests>=2.28.0',
    'PyAudio>=0.2.11',
    'websocket-client>=1.3.2'
  ],
  classifiers=[
      "Programming Language :: Python :: 3.9",
      "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  ],
)
