import os
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
  name = 'django_aws_zip',
  packages = ['django_aws_zip'],
  version = '0.3',
  description = 'A simple Django app to unzip on AWS S3.',
  author = 'Paulo Henrique da Silva',
  author_email = 'phs.paulohenriquesilva@gmail.com',
  url = 'https://github.com/paulohesilva/django_aws_zip.git', # use the URL to the github repo
  keywords = ['aws', 's3', 'zip'], # arbitrary keywords
  classifiers = [],
)