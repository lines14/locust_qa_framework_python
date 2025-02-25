from http import HTTPStatus
from main.base_test import BaseTest
from assertions import assert_response_status, assert_truth, assert_json
from main.utils.data.data_utils import DataUtils
from main.utils.data.config_manager import ConfigManager
from tests.API.JSONPlaceholder_API import JSONPlaceholderAPI

class TestAPI(BaseTest):
    JSONPlaceholder_API = JSONPlaceholderAPI()

    @classmethod
    def test_users(cls):
        response = cls.JSONPlaceholder_API.get_users(1)
        assert_response_status(response.status_code, HTTPStatus.OK)
        assert_truth(DataUtils.is_JSON(response.json()), 'response is json')

    @classmethod
    def test_posts(cls):
        response = cls.JSONPlaceholder_API.get_posts()
        assert_response_status(response.status_code, HTTPStatus.OK)
        assert_truth(DataUtils.is_JSON(response.json()), 'response is json')
        response = cls.JSONPlaceholder_API.get_posts(100)
        assert_response_status(response.status_code, HTTPStatus.OK)
        assert_json(response.json(), ConfigManager.get_test_data().resourceToCompare)
        response = cls.JSONPlaceholder_API.post_posts(ConfigManager.get_test_data().resourceToAdd)
        assert_response_status(response.status_code, HTTPStatus.CREATED)