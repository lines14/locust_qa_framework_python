from main.utils.API.base_API import BaseAPI
from main.utils.data.config_manager import ConfigManager

class JSONPlaceholderAPI(BaseAPI):
    def __init__(self, base_URL=None, log_string=None):
        super().__init__(
            base_URL or '' or ConfigManager.get_API_config_data().API_base_URL, 
            log_string or '[info] ▶ set base API URL', 
            ConfigManager.get_config_data().wait_time
        )

    def get_posts(self, id=None):
        if id:
            return super().get(f'{ConfigManager.get_API_endpoint().posts}/{id}')
        else:
            return super().get(ConfigManager.get_API_endpoint().posts)
        
    def get_users(self, id=None):
        if id:
            return super().get(f'{ConfigManager.get_API_endpoint().users}/{id}')
        else:
            return super().get(ConfigManager.get_API_endpoint().users)

    def post_posts(self, model):
        return super().post(ConfigManager.get_API_endpoint().posts, model)