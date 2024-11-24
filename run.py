import sys
import uvicorn

args = sys.argv

host = "127.0.0.1"
if len(args) > 1:
    host = args[1]

if __name__ == "__main__":
    uvicorn.run(
        "summative.API.prediction:app",
        host=host,
        port=8000,
        reload=True
    )
