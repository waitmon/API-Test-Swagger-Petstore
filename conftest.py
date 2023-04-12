from json_data import *
from pytest_voluptuous import S
import pytest
from random import randint
import requests
import random
import string

base_url = 'https://petstore.swagger.io/v2'
headers = {"accept": "application/json", "Content-Type": "application/json"}


