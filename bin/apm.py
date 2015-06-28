# coding: utf-8

import sh
import re
import os


class Apm(object):
    """
    Apm help:
        
        apm upload
        apm download
        apm sync
    """

    def __init__(self):
        pass

    @property
    def list(self):
        """ list local packages """
        local_list = sh.apm('list')
        local_list = re.search(r'atom/packages[\s\S]*$', local_list.stdout).group(0)
        local_list = re.findall(r' ([0-9a-zA-Z_-]+)@([0-9\.]+)\n', local_list)
        return local_list

    @property
    def stars(self):
        """ list stars packages """
        cloud_list = sh.apm('stars')
        cloud_list = re.findall(r'\[33m([0-9a-zA-Z_-]+)\x1b\[39m([^\x1b]*)[^\d]*(\d+)[^\d]*(\d+)', cloud_list.stdout)
        return cloud_list

    def upload(self):
        local_set = set([i[0] for i in self.list])
        cloud_set = set([i[0] for i in self.stars])
        diff_set = local_set - cloud_set
        for pkg in diff_set:
            os.system('apm star {}'.format(pkg))

    def download(self):
        local_set = set([i[0] for i in self.list])
        cloud_set = set([i[0] for i in self.stars])
        diff_set = cloud_set - local_set
        for pkg in diff_set:
            os.system('apm install {}'.format(pkg))

    def sync(self):
        self.upload()
        self.download()


def main(*args):
    apm = Apm()
    if not args:
        print help(apm.__doc__)
    getattr(apm, args[0])()

if __name__ == '__main__':
    apm = Apm()
    apm.sync()
