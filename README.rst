=====
Django AWS Zip
=====
.. image:: https://travis-ci.org/paulohesilva/django-aws-zip.svg?branch=master 
.. image:: https://readthedocs.org/projects/django-aws-zip/badge/?version=latest


django-aws-zip is a simple Django app to unzip files on AWS S3.

Quick start
-----------

1. Install::

    pip install django-aws-zip

2. Add "django-aws-zip" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_aws_zip',
    ]

3. Add AWS S3 credentials in your setings like this::

    AWS_S3_ACCESS_KEY_ID = 'YOUR_AWS_S3_ACCESS_KEY_ID'
    AWS_S3_SECRET_ACCESS_KEY = 'YOUR_AWS_S3_SECRET_ACCESS_KEY'

4. Add bucket in your settings like this::

    AWS_STORAGE_BUCKET_NAME = 'YOUR_AWS_STORAGE_BUCKET_NAME'

5. Apply migrate::

    python manage.py migrate

Code example
-------------

Example::

    from django_aws_zip.aws import Manager
    manager = Manager()
    manager.unzip('your/folder/on/aws')

