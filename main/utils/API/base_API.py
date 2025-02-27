from requests_toolbelt import sessions
from main.utils.log.logger import Logger

class BaseAPI:
    def __init__(self, base_URL, log_string, timeout=None, headers=None):
        if log_string:
            Logger.log(f'{log_string} {base_URL}')
        self.session = sessions.BaseUrlSession(base_url=base_URL)
        self.timeout = timeout
        self.headers = headers

    def get(self, endpoint):
        Logger.log(f'[info] ▶ get {endpoint}:')
        response = self.session.get(endpoint, headers=self.headers)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response

    def post(self, endpoint, params):
        Logger.log(f'[info] ▶ post {params} to {endpoint}:')
        response = self.session.post(endpoint, json=params, headers=self.headers)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response

    def put(self, endpoint, params):
        Logger.log(f'[info] ▶ put {params} to {endpoint}')
        response = self.session.put(endpoint, json=params, headers=self.headers)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response

    def patch(self, endpoint, params):
        Logger.log(f'[info] ▶ patch {params} to {endpoint}')
        response = self.session.patch(endpoint, json=params, headers=self.headers)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response

    def delete(self, endpoint):
        Logger.log(f'[info] ▶ delete {endpoint}')
        response = self.session.delete(endpoint, headers=self.headers)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response