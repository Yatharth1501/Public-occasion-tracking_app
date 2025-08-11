from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Report(BaseModel):
    title: str
    desc: str
    lat: float
    lon: float
    severity: str

reports = []

@app.post("/reports")
def create_report(report: Report):
    reports.append(report)
    return {"message": "Report added!", "total": len(reports)}

@app.get("/reports")
def list_reports():
    return [report.dict() for report in reports]

#now to check it go to the terminal and open dir in terminal then write :-

# uvicorn main:app --reload ---- (1)

# we also --host,--port if required , in the given above main is file name and app is var equal to the FastAPI() in the code

#after  running (1) go to chrome and copy paste url to check reports