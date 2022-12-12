from fastapi import FastAPI, BackgroundTasks, UploadFile
from fastapi.responses import FileResponse
from pathlib import Path
import tempfile
import shutil
import cv2
import numpy
import mimetypes


app = FastAPI()

@app.post('/picture/invert')
async def picture_invert(background_tasks: BackgroundTasks, file: UploadFile):
    Path("tmp").mkdir(parents=True, exist_ok=True)
    tempFileName = "tmp/" + next(tempfile._get_candidate_names()) + ".jpg"
    with open(tempFileName, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        img = cv2.imread(tempFileName)
        img = numpy.invert(img)
        cv2.imwrite(tempFileName, img)
    return FileResponse(tempFileName, media_type=mimetypes.guess_type(tempFileName)[0])

