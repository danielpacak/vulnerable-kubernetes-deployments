import subprocess

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fibonacci import fibonacci
import pyroscope
import os

app = FastAPI()


@app.get("/")
async def async_root_handler():
    return {"message": "Hello World"}


@app.get("/hello")
async def async_hello_handler():
    return {"hello": "world"}


@app.get("/fibonacci/recursive/{n}")
def fibonacci_recursive_handler(n: int):
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


@app.post("/linux/subprocess/run")
def linux_subprocess_run_handler(request: ProcessRequest) -> ProcessResponse:
    completed_process = subprocess.run(request.args, capture_output=True)
    return ProcessResponse(
        return_code=completed_process.returncode,
        stdout=completed_process.stdout,
        stderr=completed_process.stderr,
    )


@app.post("/linux/subprocess/run/{n}/times")
def linux_subprocess_run_n_times_handler(request: ProcessRequest, n: int):
    results = []
    for _ in range(n):
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
def python_eval_handler(request: EvalRequest):
    x = eval(request.expression)
    return {"result": x}


@app.post("/python/eval/{n}/times")
def python_eval_n_times_handler(request: EvalRequest, n: int):
    results = []
    for _ in range(n):
        results.append(eval(request.expression))
    return {"results": results}


@app.get("/python/eval/subprocess/run/id")
def python_eval_subprocess_run_id_handler():
    out = eval("__import__('subprocess').run('id')")
    return {"stdout": out}


@app.get("/python/eval/os/system/id")
def python_eval_os_system_id_handler():
    out = eval("__import__('os').system('id')")
    return {"stdout": out}


@app.get("/health")
def health_handler():
    return {"status": "healthy"}


# Configure Grafana PyroscopeSDK
# docker run --rm -d --name pyroscope -p 4040:4040 grafana/pyroscope
pyroscope_application_name = (
    os.getenv("PYROSCOPE_APPLICATION_NAME") or "hello-fastapi-python3.9"
)
pyroscope_server_address = (
    os.getenv("PYROSCOPE_SERVER_ADDRESS") or "http://localhost:4040"
)

pyroscope.configure(
    application_name=pyroscope_application_name,
    server_address=pyroscope_server_address,
    enable_logging=True,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
