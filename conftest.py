from random import randint
import pytest
import requests
import random
from json_data import *
import string
from mimesis import Person
from mimesis.builtins import en
from pytest_voluptuous import S

base_url = 'https://petstore.swagger.io/v2'
headers = {"accept": "application/json", "Content-Type": "application/json"}


