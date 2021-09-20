import os
from fastapi import FastAPI
import openai
from typing import Optional, Set
from pydantic import BaseModel

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class RequestCompletionItem(BaseModel):
    engine: Optional[str] = None
    prompt: str
    max_tokens: Optional[int] = None
    temperature: Optional[int] = None
    top_p: Optional[int] = None
    frequency_penalty: Optional[int] = 0
    presence_penalty: Optional[int] = 0
    logprobs: Optional[int] = None
    best_of: Optional[int] = 1
    echo: Optional[bool] = False
    stop: Optional[list] = None


@app.get("/gpt3_engines")
def get_engines():
    engines = openai.Engine.list()
    return engines

@app.get("/gpt3_completion_async", summary = "Create an item")
async def get_completion_async(item: RequestCompletionItem):
    """
    Async function for create an item-completion (In test)

    - **engine**: engine identification
    - **prompt**: a long description
    - **max_tokens**: integer non required
    - **temperature**: float between 0 and 1 https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277
    - **top_p**: float between 0 and 1
    - **frequency_penalty**: float between 0 and 1
    - **presence_penalty**: float between 0 and 1
    - **logprobs**: integer non required (Include the log probabilities on the logprobs most likely tokens, as well the chosen tokens.)
    - **best_of**: integer non required (Generates best_of completions server-side and returns the "best" )
    - **stop**: list non required (Up to 4 sequences where the API will stop generating further tokens.)
    - **echo**: boolean non required (Echo back the prompt in addition to the completion)
    \f
    :param item: User input.
    """
    completion = openai.Completion.create(
        engine=item.engine, 
        prompt=item.prompt,
        max_tokens=item.max_tokens,
        temperature=item.temperature,
        top_p=item.top_p,
        frequency_penalty=item.frequency_penalty,
        presence_penalty=item.presence_penalty,
        logprobs=item.logprobs,
        best_of=item.best_of,
        stop=item.stop,
        echo=item.echo)
    return completion.choices

@app.get("/gpt3_completion", summary = "Create an item")
def get_completion(item: RequestCompletionItem):
    """
    sync function for create an item-completion:

    - **engine**: engine identification
    - **prompt**: a long description
    - **max_tokens**: integer non required
    - **temperature**: float between 0 and 1 https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277
    - **top_p**: float between 0 and 1
    - **frequency_penalty**: float between 0 and 1
    - **presence_penalty**: float between 0 and 1
    - **logprobs**: integer non required (Include the log probabilities on the logprobs most likely tokens, as well the chosen tokens.)
    - **best_of**: integer non required (Generates best_of completions server-side and returns the "best" )
    - **stop**: list non required (Up to 4 sequences where the API will stop generating further tokens.)
    - **echo**: boolean non required (Echo back the prompt in addition to the completion)
    \f
    :param item: User input.
    """
    completion = openai.Completion.create(
        engine=item.engine, 
        prompt=item.prompt,
        max_tokens=item.max_tokens,
        temperature=item.temperature,
        top_p=item.top_p,
        frequency_penalty=item.frequency_penalty,
        presence_penalty=item.presence_penalty,
        logprobs=item.logprobs,
        best_of=item.best_of,
        stop=item.stop,
        echo=item.echo)
    return completion.choices
