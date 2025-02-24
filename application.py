from server import app

if __name__ == "__server__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
