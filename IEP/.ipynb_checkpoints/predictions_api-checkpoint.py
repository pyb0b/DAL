try:
    import uvicorn
    
    from fastapi import FastAPI, UploadFile, File, HTTPException
    from fastapi.middleware.cors import CORSMiddleware
    
    import requests

except Exception as e:
   print('Error loading module in predictions.py: ', e)

app = FastAPI(title='Assentify')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    API_URL_cancer = "https://api-inference.huggingface.co/models/MUmairAB/Breast_Cancer_Detector"
    headers_cancer = {"Authorization": "Bearer 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"}
    
    API_URL_pneumo = "https://api-inference.huggingface.co/models/dima806/chest_xray_pneumonia_detection"
    headers_pneumo = {"Authorization": "Bearer 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"}
    
    API_URL_fract = "https://api-inference.huggingface.co/models/nandodeomkar/autotrain-bone-fracture-detection-54370127369"
    headers_fract = {"Authorization": "Bearer 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"}
except Exception as e:
   print('Connection error: ', e)


@app.post("/query_cancer")
async def query_cancer(filename: UploadFile =File(...)):
    try:
        contents = await filename.read()
        response = requests.post(API_URL_cancer, headers=headers_cancer, data=contents)
        return response.json()
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))     


@app.post("/query_pneumo")
async def query_pneumo(filename: UploadFile =File(...)):
    try:
        contents = await filename.read()
        response = requests.post(API_URL_pneumo, headers=headers_pneumo, data=contents)
        return response.json()
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query_fracture")
async def query_fracture(filename: UploadFile =File(...)):
    try:
        contents = await filename.read()
        response = requests.post(API_URL_fract, headers=headers_fract, data=contents)
        return response.json()
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)