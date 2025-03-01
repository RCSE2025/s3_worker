Библиотеки:
```txt
annotated-types==0.7.0
anyio==4.4.0
boto3==1.34.116
botocore==1.34.116
certifi==2024.2.2
click==8.1.7
dnspython==2.6.1
email_validator==2.1.1
exceptiongroup==1.2.1
fastapi==0.111.0
fastapi-cli==0.0.4
h11==0.14.0
httpcore==1.0.5
httptools==0.6.1
httpx==0.27.0
idna==3.7
Jinja2==3.1.4
jmespath==1.0.1
markdown-it-py==3.0.0
MarkupSafe==2.1.5
mdurl==0.1.2
orjson==3.10.3
pydantic==2.7.2
pydantic_core==2.18.3
Pygments==2.18.0
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
python-multipart==0.0.9
PyYAML==6.0.1
rich==13.7.1
s3transfer==0.10.1
shellingham==1.5.4
six==1.16.0
sniffio==1.3.1
starlette==0.37.2
typer==0.12.3
typing_extensions==4.12.0
ujson==5.10.0
urllib3==2.2.1
uvicorn==0.30.0
uvloop==0.19.0
watchfiles==0.22.0
websockets==12.0
```

Запуск на localhost:
1. ```sh
   docker compose up
   ```
2. Зайти в панель minio по адресу http://localhost:9001 (логин - `minioadmin`, пароль - `minioadmin`)
3. Во вкладке Access Keys создать новый ключ
4. Созданный ключ прописать в `docker-compose.yml` в переменные `MINIO_ACCESS_KEY` и `MINIO_SECRET_KEY`
5. В переменную `MINIO_PUBLIC_URL` прописать `http://localhost:9000`
6. ```sh
   docker compose restart
   ```
