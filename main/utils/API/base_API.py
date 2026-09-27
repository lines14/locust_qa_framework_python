import httpx

from main.utils.log.logger import Logger


class BaseAPI:
    def __init__(self, base_url, timeout=None, headers=None, log_string=None, verify=None):
        if log_string:
            Logger.log(f"{log_string} {base_url}")
        self.client = httpx.Client(
            base_url=base_url,
            headers=headers,
            timeout=timeout,
            verify=verify if verify is not None else True,
        )

    def set_bearer_token(self, token: str):
        auth_header = {"Authorization": f"Bearer {token}"}
        self.client.headers.update(auth_header)
        return auth_header

    def get(self, endpoint, params=None):
        Logger.log(f"[req] ▶ get {params or {}} from {endpoint}:")
        response = self.client.get(endpoint, params=params)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response

    def post(self, endpoint, data=None):
        Logger.log(f"[req] ▶ post {data or {}} to {endpoint}:")
        response = self.client.post(endpoint, json=data)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response

    def put(self, endpoint, data=None):
        Logger.log(f"[req] ▶ put {data or {}} to {endpoint}:")
        response = self.client.put(endpoint, json=data)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response

    def patch(self, endpoint, data=None):
        Logger.log(f"[req] ▶ patch {data or {}} to {endpoint}:")
        response = self.client.patch(endpoint, json=data)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response

    def delete(self, endpoint):
        Logger.log(f"[req] ▶ delete {endpoint}:")
        response = self.client.delete(endpoint)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response
