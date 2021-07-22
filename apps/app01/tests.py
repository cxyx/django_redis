from django.test import TestCase

# Create your tests here.

import os
def create_dir_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)


create_dir_not_exist('./time.txt')

with open('time.txt') as f:
    f.write('123')