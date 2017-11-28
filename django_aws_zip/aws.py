import boto
import zipfile
import os
import shutil
from threading import Thread
from django.conf import settings
from .models import Task


class Manager(object):

    def unzip(self, key):
        if not Task.objects.filter(key=key, status=0):
            self.zip = ZipThread(key)
            self.zip.start()
            return self.zip.get_task_id()

        return Task.objects.get(key=key, status=0).id

    def get_unzip_id(self, key):
        return Task.objects.get(key=key, status=0).id

    def get_unzip_percent(self, key):
        return Task.objects.get(key=key, status=0).percent

class ZipThread(Thread):

    def __init__(self, key):
        Thread.__init__(self)
        # self.key = key
        self.task = Task.objects.create(key=key)

    def get_task_id(self):
        return self.task.id

    def run(self):
        print('Star job zip for key: '+self.task.key)
        zip = S3Zip(self.task)
        zip.unzip(self.task.key)


class S3Zip(object):

    def __init__(self, task=None):
        self.KEY = getattr(settings, 'AWS_S3_ACCESS_KEY_ID', None)
        self.SECRET = getattr(settings, 'AWS_S3_SECRET_ACCESS_KEY', None)
        self.BUCKET = getattr(settings, 'AWS_STORAGE_BUCKET_NAME', None)
        self.task = task
        if not self.KEY or not self.SECRET or not self.BUCKET:
            raise Exception

    def zip(self):
        pass

    def unzip(self, key):
        print('Recovering file                      5%..')
        self._download_s3_file(key)
        print('Unpacking                            10%....')
        filename = self._get_filename_by_key(key)
        self._unzip_local(filename)
        print('Creating structure and setting       70%......')
        self._send(key, filename)
        print('Remove temporary files               80%.......')
        self._remove_tmp('tmp/'+filename)
        self._remove_tmp(filename)
        print('Finish                               100%...........')


    def _unzip_local(self, path_to_zip_file):
        zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
        zip_ref.extractall('tmp/'+zip_ref.filename+'/')
        zip_ref.close()
        return zip_ref.filename

    def _get_file_list(self, path):
        zfobj = zipfile.ZipFile(path)
        self.name_list = {zfobj.filename: zfobj.namelist()}
        self.total_items = len(zfobj.namelist())
        return self.name_list

    def _send(self, keypath, path):
        filename = self._unzip_local(path)
        unz_stricture = self._get_file_list(path)
        current_file = 0
        for key, values in unz_stricture.items():
            for val in values:
                self._create_content(keypath+'/' + val, 'tmp/' + filename+ '/' + val)
                current_file = (current_file + 1)
                # print(str(current_file) + ' of ' + str(self.total_items))
                print('Progress:' + str((100 *(int(current_file)/int(self.total_items))))+'%')

                if self.task is not None:
                    self.task.percent = (100 *(int(current_file)/int(self.total_items)))
                    self.task.save()
        self.task.status = 1
        self.task.save()

    def _create_content(self, key, content=None):
        try:
            s3 = boto.connect_s3(self.KEY, self.SECRET)
            bucket = s3.get_bucket(self.BUCKET)
            k = bucket.new_key(key)
            if content is not None:
                k.set_contents_from_filename(content)

        except IsADirectoryError as e:
            self.set_log(str(e))

        except Exception as e:
            self.set_log(str(e))
            self.task.status = 2

    def _download_s3_file(self, key):
        s3 = boto.connect_s3(self.KEY, self.SECRET)
        bucket = s3.get_bucket(self.BUCKET)
        s3_path = str(key)
        try:
            k = bucket.get_key(s3_path)
            filename = self._get_filename_by_key(s3_path)
            k.get_contents_to_filename(filename)
        except (OSError) as e:
            print(str(e))
            self.task.status = 2
            return False

    def _remove_tmp(self, path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)

    def _get_filename_by_key(self, key):
        filename_arr = key.split('/')
        filename = filename_arr[len(filename_arr)-1]
        return filename

    def set_log(self, log):
        with open('unzip_file_log.dat', 'a') as file:
            file.write(log + '\n')
