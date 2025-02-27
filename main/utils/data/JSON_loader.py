import os
import json
import classutilities
from main.utils.data.data_utils import DataUtils
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class JSONLoader():
    @classutilities.classproperty
    def config_data(cls):
        with open('../../../resources/config_data.json', 'r', encoding='utf-8') as data:
            return DataUtils.dict_to_model(json.loads(data.read()))
        
    @classutilities.classproperty
    def API_endpoints(cls):
        with open('../../../resources/API_endpoints.json', 'r', encoding='utf-8') as data:
            return DataUtils.dict_to_model(json.loads(data.read()))