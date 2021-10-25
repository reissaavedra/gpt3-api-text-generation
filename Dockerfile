FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install openai pydantic typing

ARG OPENAI_API_KEY=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

COPY ./app /app