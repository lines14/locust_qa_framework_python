import json
import os

from main.utils.data.data_utils import DataUtils

_RESOURCES_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../resources/data"))


class JSONLoader:
    @classmethod
    def load_all(cls):
        for file_name in os.listdir(_RESOURCES_DIR):
            if file_name.endswith(".json"):
                attr_name = os.path.splitext(file_name)[0]
                with open(os.path.join(_RESOURCES_DIR, file_name), encoding="utf-8") as json_file:
                    setattr(cls, attr_name, DataUtils.dict_to_model(json.loads(json_file.read())))
