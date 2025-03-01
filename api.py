from fastapi import FastAPI, Query, UploadFile, Request, status
from fastapi.responses import JSONResponse
from worker import S3Worker, File
from worker.config import MINIO_PUBLIC_URL
from worker.exceptions.WorkerException import WorkerException
import urllib.parse

Worker = S3Worker()

app = FastAPI()


@app.exception_handler(WorkerException)
async def worker_exception_handler(_: Request, exception: WorkerException):
    return JSONResponse(
        status_code=400,
        content={"message": str(exception)}
    )


@app.post("/new_bucket", status_code=status.HTTP_204_NO_CONTENT, tags=["Buckets"])
async def new_bucket(name: str):
    Worker.new_bucket(name)


@app.delete("/remove_bucket", status_code=status.HTTP_204_NO_CONTENT, tags=["Buckets"])
async def remove_bucket(name: str):
    Worker.remove_bucket(name)


@app.get("/files/{bucket}", tags=["Files", "Buckets"])
async def list_files(bucket: str) -> list[str]:
    return Worker.list_files(bucket)


@app.post("/upload_file", tags=["Files"])
async def upload_file(bucket: str,
                      file: UploadFile,
                      filename: str | None = Query(None),
                      mimetype: str | None = None) -> str:
    return Worker.upload_file(bucket,
                              File(urllib.parse.unquote(filename or file.filename),
                                   mimetype or file.content_type,
                                   file.file))


@app.delete("/remove_file", status_code=status.HTTP_204_NO_CONTENT, tags=["Files"])
async def remove_file(bucket: str, filename: str = Query()):
    Worker.remove_file(bucket, filename)


@app.get("/file/{bucket}/{filename:path}", tags=["Files"])
async def get_file_url(bucket: str, filename: str) -> str:
    url = Worker.get_file_url(bucket, filename)
    url = url.replace("http://host.docker.internal:9000", MINIO_PUBLIC_URL)
    return url


@app.post("/files/{bucket}", tags=["Files"])
async def get_files_urls(bucket: str, filenames: list[str]) -> dict[str, str]:
    return Worker.get_files_urls(bucket, filenames)
