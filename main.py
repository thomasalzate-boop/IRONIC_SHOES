import webbrowser
from pathlib import Path

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    html_file = Path(__file__).parent / "IRONIC_SHOES" / "index.html"
    webbrowser.open(html_file.resolve().as_uri())
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

