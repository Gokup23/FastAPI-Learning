from fastapi import FastAPI

app = FastAPI()

gate_da_syllabus = [
    {"id": 1, "subject": "Math", "topic": "Linear Algebra", "status": "completed", "weightage": "high"},
    {"id": 2, "subject": "Math", "topic": "Calculus", "status": "pending", "weightage": "high"},
    {"id": 3, "subject": "AI", "topic": "Search Algorithms", "status": "learning", "weightage": "medium"},
    {"id": 4, "subject": "ML", "topic": "Regression", "status": "completed", "weightage": "high"},
    {"id": 5, "subject": "ML", "topic": "Clustering", "status": "pending", "weightage": "medium"},
    {"id": 6, "subject": "DB", "topic": "SQL", "status": "completed", "weightage": "low"}
]

# 1. THE MASTER LIST
@app.get("/syllabus")
async def syllabus():
    return gate_da_syllabus

# 2. THE PATH PARAMETER (Deep Dive)
@app.get("/syllabus/{topic_id}")
async def syll_specific(topic_id: int): # <-- Let the function receive the ID
    
    # Loop through our database
    for item in gate_da_syllabus:
        # Check if the dictionary's 'id' matches the URL's topic_id
        if item["id"] == topic_id:
            return item
            
    # If the loop finishes and finds nothing, return the error
    return {"error": "Topic not found"}

# 3. THE QUERY PARAMETERS (Filter Engine)
@app.get("/topics/")
async def custom(status: str = None, weightage: str = None):
    # Start with the full list
    filtered_list = gate_da_syllabus
    
    # If the user typed ?status=something, filter the list
    if status:
        filtered_list = [item for item in filtered_list if item["status"] == status]
        
    # If the user typed ?weightage=something, filter the list again
    if weightage:
        filtered_list = [item for item in filtered_list if item["weightage"] == weightage]
        
    return filtered_list