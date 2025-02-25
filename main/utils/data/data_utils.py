from main.utils.log.logger import Logger

class DataUtils:
    @staticmethod
    def is_JSON(API_response):
        Logger.log('[info] ▶ check API response is JSON')
        if type(API_response) == list:
            return type(API_response.pop()) == dict
        else:
            return type(API_response) == dict
    
    @staticmethod
    def model_to_dict(model):
        return {key: value for key, value in vars(model).items() if not key.startswith('__')}

    @staticmethod
    def dict_list_to_models_list(dict_list):
        Logger.log('[info] ▶ get models from JSON')
        return list(map(lambda element: type("Model", (object, ), element), dict_list))

    @staticmethod
    def data_to_models(parent_class, data_matrix, rows_count=1, counter=0):
        models_list = []
        if rows_count > 1:
            Logger.log('[info] ▶ get models from table')
        while counter < rows_count:
            model_fields = list(filter(lambda attr: not attr.startswith("__"), dir(parent_class)))
            model_dict = dict.fromkeys(model_fields)
            for key in model_dict:
                model_dict[key] = data_matrix[counter][model_fields.index(key)]
            model = type("Model", (object, ), model_dict)
            models_list.append(model)
            counter += 1

        return models_list