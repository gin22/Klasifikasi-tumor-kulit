from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StarticFiles
from starlette.middleware.cors import CORSMidlleware
import uvicorn, aiohttp, asyncio
from io import BytesIO

from fastai import *
from fastai.vision import*

# Change the export_file_url. I used Google Drive link:              
export_file_url =  'https://drive.google.com/file/d/1g0ZbeWZFgU7mL-0EmbOminZ0jeF-kUpu/view?usp=sharing'                       
#Write the model's name:
export_file_name = 'model_klasifikasi_tumor.pkl' 
#Write all the classes:
                                              
classes = ['Tumor Ganas', 'Tumor Jinak']

path = Path(__file__).parent
