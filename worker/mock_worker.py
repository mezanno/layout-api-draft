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

# Load the mock json payload
import json
with open("mock_data.json") as f:
    mock_data = json.load(f)

@app.get("/layout")
async def layout(
    image_url: str,
    auto_deskew: bool = False,
    auto_bg_removal: bool = True,
    auto_denoise: bool = True,
    text_x_height_pixels: int = -1,
    try_download_image: bool = False,
    ):

    # Debug output
    print(f"image_url: {image_url}")

    if try_download_image:
        async with httpx.AsyncClient() as client:
            response = await client.get(image_url, timeout=10.0)
            if response.status_code == 200:
                return {"message": "ok", "status_code": response.status_code, "data_len": len(response.content)}
            else:
                return {"message": "image server error", "status_code": response.status_code}
    
    return mock_data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
