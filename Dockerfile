FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install openai pydantic typing

COPY ./app /app