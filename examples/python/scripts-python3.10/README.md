# Python 3.10 Scripts

```
uv venv -p 3.10
```

```
source .venv/bin/activate
```

## eval.py

```
------------------- New Sample --------------------
  thread.name: python
  process.executable.name: python3.10
  process.executable.path: /usr/bin/python3.10
  process.pid: 115554
  thread.id: 115554
---------------------------------------------------
Instrumentation: native: Function: 0x153ae3, File: python3.10
Instrumentation: native: Function: 0x200bd7, File: python3.10
Instrumentation: native: Function: 0x27b95a, File: python3.10
Instrumentation: native: Function: 0x27b69e, File: python3.10
Instrumentation: native: Function: 0x2752e0, File: python3.10
Instrumentation: native: Function: 0x27dbc3, File: python3.10
Instrumentation: native: Function: 0x18b418, File: python3.10
Instrumentation: cpython, Function: function_with_infinite_loop, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/eval.py, Line: 5, Column: 0
Instrumentation: cpython, Function: top_level_function, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/eval.py, Line: 11, Column: 0
Instrumentation: cpython, Function: <module>, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/eval.py, Line: 4, Column: 0
------------------- End Sample --------------------
```

## fibonacci.py

```
------------------- New Sample --------------------
  thread.name: python
  process.executable.name: python3.10
  process.executable.path: /usr/bin/python3.10
  process.pid: 112976
  thread.id: 112976
---------------------------------------------------
Instrumentation: native: Function: 0x1a0f27, File: python3.10
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 5, Column: 0
Instrumentation: cpython, Function: <module>, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-scripts/fibonacci.py, Line: 4, Column: 0
------------------- End Sample --------------------
```