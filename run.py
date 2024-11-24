import os
import sys
import uvicorn

args = sys.argv

port = int(os.getenv("PORT", 8000))
host = "127.0.0.1"

if len(args) > 1:
    host = args[1]

if __name__ == "__main__":
    uvicorn.run(
        "summative.API.prediction:app",
        host=host,
        port=port,
        reload=True
    )
