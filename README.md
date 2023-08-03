# TranscriptAssist
TranscriptAssist is a Python package that combines Google Cloud Vision API, Mathpix OCR API, and OpenAI's GPT-4 to transcribe images of handwritten math into LaTeX.

# Installation
```bash
pip install -r requirements.txt
```

# Setup
### Add credentials to .env file in root directory of project
```bash
# MathPix
MATHPIX_APP_KEY=""
MATHPIX_APP_ID=""
# Google Cloud Vision
GOOGLE_CLOUD_API_KEY=""
GOOGLE_CLOUD_APP_ID=""
# OpenAI
OPENAI_API_KEY=""
```

# Usage
### 1. Import TranscriptAssist 
```python
from transcriptassist.transcriptassist import TranscriptAssist
```
### 2. Initialize a TranscriptAssist object
- **temperature** (float): 
  - The temperature to use for the GPT model.
  - default: 0.3
```python
ta = TranscriptAssist(temperature)
```

### 3. Transcribe an image
- **link_or_path** (str):
  - The link or path of the image to transcribe. 
- **crop_coordinates** (tuple): 
  - The coordinates to crop the image to. 
  - format: (x1, y1, x2, y2)
  - default: None
- **use_gcv** (bool):
  - Whether to use Google Cloud Vision API.
  - default: True
- **use_mathpix** (bool):
    - Whether to use Mathpix API.
    - default: True

```python
ta.transcribe(link_or_path, crop_coordinates, use_gcv, use_mathpix)
```

