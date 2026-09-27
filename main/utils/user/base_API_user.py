from locust import HttpUser

from config import Config
from main.utils.user.base.base_user import BaseUser


class BaseAPIUser(BaseUser, HttpUser):
    abstract = True
    host = Config().base_url
