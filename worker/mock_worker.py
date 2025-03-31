from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import httpx

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/layout")
async def layout(image_url: str, auto_deskew: bool = False, auto_bg_removal: bool = True, auto_denoise: bool = True, text_x_height_pixels: int = -1):
    # Parse the URL which should have the following format:
    # https://openapi.bnf.fr/iiif/image/v3/ark:/12148/bd6t543045578/f5/full/max/0/default.webp
    # We will replace the "https://openapi.bnf.fr" part with "http://cache"
    url = image_url.replace("https://openapi.bnf.fr", "http://cache/gallica")

    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=10.0)
        if response.status_code == 200:
            return {"message": "ok", "status_code": response.status_code, "data_len": len(response.content)}
        else:
            return {"message": "cache server error", "status_code": response.status_code}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
