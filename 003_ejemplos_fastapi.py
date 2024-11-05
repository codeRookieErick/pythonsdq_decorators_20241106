from fastapi import FastAPI
import uvicorn

app = FastAPI()

#https://github.com/fastapi/fastapi/blob/d4ab06a2b6b59bd264c0cc43367c5a68174e8f88/fastapi/routing.py#L869
#App tiene un Router > Metodo llamado get > Decorator factory route

@app.get('example')
def example_endpoint():
    return {
        "Message": "Todo bien"
    }

uvicorn.run(app, host='0.0.0.0', port=8080)