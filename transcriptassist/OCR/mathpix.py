import requests
import json
import re

class MathPix:
    def __init__(self, APP_KEY, APP_ID):
        self.credentials = {"app_id": APP_ID, "app_key": APP_KEY}

    def get_all_text(self, path):
        files = {"file": open(path, "rb")}
        data = {
            "options_json": json.dumps({
                "formats": ["text"]
            })
        }
        r = requests.post("https://api.mathpix.com/v3/text", files=files, data=data, headers=self.credentials)
        try:
            return r.json()["text"]
        except:
            return None

