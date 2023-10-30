"""data_tools contains functions for loading and manipulating data."""

from pydantic import BaseModel
from datetime import date
from pathlib import Path
import yaml

class Info(BaseModel):
    """Info contains personal information with a key name and a value."""
    name: str
    value: str
    alias: list[str]

class Experience(BaseModel):
    """Experience contains information about education or work experience."""
    name: str
    institution: str
    place: str
    description: list[str]
    start: date
    end: date

class Languages(BaseModel):
    """Language contains information about a language."""
    name: str
    level: str

class Resume(BaseModel):
    """Resume contains all data for a resume."""
    info: list[Info]
    education: list[Experience]
    experience: list[Experience]
    technologies: list[str]
    tools: list[str]
    hobbies: list[str]
    languages: list[Languages]
    skills: list[str]

def load_resume(file: str) -> Resume:
    """Loads a resume from a YAML file."""
    file_path = Path(file)
    with open(file_path, "r") as f:
        resume = yaml.safe_load(f)
    return Resume(**resume)

if __name__ == "__main__":
    resume = load_resume("lucas-data.yaml")
    print(resume)
