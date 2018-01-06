from django.test import TestCase
from urllib import request
# Create your tests here.

req = request.urlopen('127.0.0.0:8000/signup', )