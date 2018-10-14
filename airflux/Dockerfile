FROM python:3.5

WORKDIR ./airflux

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python","./airflux.py"]
