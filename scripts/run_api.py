from pathlib import Path; import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import uvicorn
if __name__ == "__main__":
    uvicorn.run("backend.api.server:app", host="127.0.0.1", port=5055, reload=False)
