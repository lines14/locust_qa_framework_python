import json

class DataUtils:            
    @classmethod
    def nested_data_to_models(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj
    
    @classmethod
    def dict_to_model(cls, dict):
        return json.loads(
            json.dumps(dict, ensure_ascii=False), 
            object_hook=cls.nested_data_to_models
        )