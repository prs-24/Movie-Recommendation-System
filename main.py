from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from recommender import recommend

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recommend", response_class=HTMLResponse)
async def get_recommendation(request: Request):
    form = await request.form()
    title = form.get("movie")

    hero, results = recommend(title)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "recommendations": results,
            "movie": title,
            "hero": hero
        }
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

