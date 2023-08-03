from google.cloud import vision


class GoogleCloudVision:
    def __init__(self, API_KEY, PROJECT_ID, verbal=False):

        self.client = vision.ImageAnnotatorClient(
            client_options={"api_key": API_KEY, "quota_project_id": PROJECT_ID}
        )

    def _process_image(self, path):
        with open(path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = self.client.document_text_detection(image=image, image_context={"language_hints": ["en"]})

        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
        return response

    def get_all_text(self, path, verbal=False):
        response = self._process_image(path)
        if verbal:
            print(response.full_text_annotation.text)
        return response.full_text_annotation.text


