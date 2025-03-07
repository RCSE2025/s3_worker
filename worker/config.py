from os import environ
from dotenv import load_dotenv

load_dotenv()

# S3
MINIO_ACCESS_KEY = environ.get("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = environ.get("MINIO_SECRET_KEY")
MINIO_ENDPOINT_URL = environ.get("MINIO_ENDPOINT_URL")
MINIO_EXPIRES_FILE_LINK_IN_SECONDS = 60 * 60 * 24 * 365 * 100 # 100 years
MINIO_PUBLIC_URL = environ.get("MINIO_PUBLIC_URL")