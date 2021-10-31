#Creating class for image data
from pydantic import BaseModel

class Image(BaseModel):
    image_path: str