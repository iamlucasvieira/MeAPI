from fastapi import FastAPI
from data_tools import load_resume
app = FastAPI()

resume_data = load_resume("lucas-data.yaml")

@app.get("/")
async def root():
    """Returns a greeting message."""
    return {"greeting": "Hello, World!", "message": "Welcome to my API!"}

@app.get("/all")
async def all():
    """Returns all the data in my resume."""
    return resume_data

@app.get("/info")
async def info():
    """Returns my contact information."""
    return resume_data.info

@app.get("/education")
async def education():
    """Returns my education background data."""
    return resume_data.education

@app.get("/experience")
async def experience():
    """Returns my work experience data."""
    return resume_data.experience

@app.get("/technologies")
async def technologies():
    """Returns the technologies I can use."""
    return resume_data.technologies

@app.get("/tools")
async def tools():
    """Returns the tools I can use."""
    return resume_data.tools

@app.get("/hobbies")
async def hobbies():
    """Returns my hobbies."""
    return resume_data.hobbies

@app.get("/languages")
async def languages():
    """Returns the languages I can speak."""
    return resume_data.languages

@app.get("/skills")
async def skills():
    """Returns my skills."""
    return resume_data.skills

@app.get("/info/{keyword}")
async def info_keyword(keyword: str):
    """Searchs for a contact information by keyword.

    Args:
        name (str): The name of the contact information.
    """
    for i in resume_data.info:
        if keyword.lower() in i.alias:
            return i
    return {"error": f"{keyword} was not found as part of my contact information."}

# Endpoint that searchs for a keywork in the resume. and returns the data
@app.get("/search/{keyword}")
async def keyword(keyword: str):
    """Searchs for a keyword in the resume."""
    result = dict(
        info=[],
        education=[],
        experience=[],
        technologies=[],
        tools=[],
        hobbies=[],
        languages=[],
        skills=[]
    )
    for i in resume_data.info:
        if keyword.lower() in i.alias:
            result["info"].append(i)
    for i in resume_data.education:
        if keyword.lower() in " ".join(i.description).lower():
            result["education"].append(i)
    for i in resume_data.experience:
        if keyword.lower() in " ".join(i.description).lower():
            result["experience"].append(i)
    for i in resume_data.technologies:
        if keyword.lower() == i.lower():
            result["technologies"].append(i)
    for i in resume_data.tools:
        if keyword.lower() == i.lower():
            result["tools"].append(i)
    for i in resume_data.hobbies:
        if keyword.lower() == i.lower():
            result["tools"].append(i)
    for i in resume_data.languages:
        if keyword.lower() == i.name.lower():
            result["languages"].append(i)
    for i in resume_data.skills:
        if keyword.lower() == i.lower():
            result["skills"].append(i)
    return result
