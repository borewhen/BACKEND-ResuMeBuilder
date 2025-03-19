from pydantic import BaseModel
from typing import List

class CourseCreateRequest(BaseModel):
    unit_names: List[str]