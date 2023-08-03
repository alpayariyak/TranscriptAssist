import base64
import io
import requests
from PIL import Image


def process_image(link_or_path, crop_coordinates, show_image=False):
    if link_or_path.startswith('http') or link_or_path.startswith('www.'):
        response = requests.get(link_or_path)
        img = Image.open(io.BytesIO(response.content))
    else:
        img = Image.open(link_or_path)
    if crop_coordinates:
        img = img.crop(crop_coordinates)  # Make sure coordinates is a tuple like (x1, y1, x2, y2)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    if show_image:
        img.show()
    return buffered.getvalue()


def generate_prompt(gcv_text, mathpix_text):
    prompt = ""
    if gcv_text:
        prompt += f"OCR-1:\n{gcv_text.strip()}\n\n"
    if mathpix_text:
        prompt += f"OCR-2:\n{mathpix_text.strip()}\n\n"
    if prompt != "":
        prompt += "Inferred Correct Transcription:\n"
    else:
        prompt = False
    return prompt
