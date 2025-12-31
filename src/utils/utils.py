class utils:
    def common_headers_json():
        headers = {
            "Content-Type": "application/json",
        }
        return headers

    def common_headers_xml(self):
        headers = {
        "Content-Type": "application/xml ",
    }
        return headers
    def common_headers_put_patch_delete_basic_auth(self,basic_auth):
        headers = {
        "Content-Type": "application/json ",
        "Authorization": "Basic " + str(basic_auth),
    }
        return headers

    def common_headers_put_patch_delete_patch_cookie(self, token: str):
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cookie": f"token={token}"
            }
            return headers
    def common_headers_put_patch_delete_patch_bearer_auth(self,api_token):
        headers = {
        "Content-Type": "application/json ",
        "Authorization": "Bearer" + str(api_token),
    }
        return headers
    def read_csv_file(self):
        pass
    def read_env_file(self):
        pass
    def read_database(self):
        pass