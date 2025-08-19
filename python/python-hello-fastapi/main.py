import subprocess
from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fibonacci import fibonacci

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello():
    return {"hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/fibonacci/{n}")
def fibonacci_rule(n: int):
    """
    This is a good test to see the limits of stack unwinding and eBPF,
    not the most efficient implementation of the Fibonacci algorithm.
    """
    return {"fibonacci": fibonacci(n)}


# It seems that subprocess.run will use clone3 system call
@app.get("/linux/process/id")
def linux_process_id():
    completed_process = subprocess.run(["id"], capture_output=True)
    return ProcessResponse(
        return_code=completed_process.returncode,
        stdout=completed_process.stdout,
        stderr=completed_process.stderr,
    )


class ProcessRequest(BaseModel):
    args: list


class ProcessResponse(BaseModel):
    return_code: int
    stdout: bytes
    stderr: bytes


@app.post("/linux/process")
def linux_process(request: ProcessRequest):
    completed_process = subprocess.run(request.args, capture_output=True)
    return ProcessResponse(
        return_code=completed_process.returncode,
        stdout=completed_process.stdout,
        stderr=completed_process.stderr,
    )


@app.post("/linux/process/n/times")
def linux_process_n_times(request: ProcessRequest, times: int = 1):
    results = []
    for _ in range(times):
        completed_process = subprocess.run(request.args, capture_output=True)
        results.append(
            ProcessResponse(
                return_code=completed_process.returncode,
                stdout=completed_process.stdout,
                stderr=completed_process.stderr,
            )
        )
    return results


class EvalRequest(BaseModel):
    expression: str


# eval("subprocess.getoutput('echo Hello, World')")
# "__import__('subprocess').getoutput('rm –rf *')"
# "__import__('subprocess').getoutput('echo Hello World')"
# "import('os').system('id')"
# "__import__('os').system('id')" <-- this is using vfork system call
# "__import__('subprocess').run('id')" <-- this is also using vfork system call???
# https://realpython.com/python-eval-function/
@app.post("/python/eval")
def python_eval(request: EvalRequest):
    x = eval(request.expression)
    return {"result": x}


@app.post("/python/eval/{n}/times")
def python_eval_n_times(request: EvalRequest, n: int = 1):
    results = []
    for _ in range(n):
        results.append(eval(request.expression))
    return {"results": results}


@app.get("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
