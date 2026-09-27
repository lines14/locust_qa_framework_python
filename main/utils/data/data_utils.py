import json


class DataUtils:
    @classmethod
    def nested_data_to_models(cls, data):
        obj = cls()
        obj.__dict__.update(data)
        return obj

    @classmethod
    def dict_to_model(cls, data):
        return json.loads(json.dumps(data, ensure_ascii=False), object_hook=cls.nested_data_to_models)
