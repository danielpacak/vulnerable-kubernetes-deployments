# Python 3.9 Scripts

```
uv venv -p 3.9
```

```
source .venv/bin/activate
```

## eval.py

```
------------------- New Sample --------------------
  thread.name: python
  process.executable.name: python3.9
  process.executable.path: /home/dpacak/.local/share/uv/python/cpython-3.9.23-linux-x86_64-gnu/bin/python3.9
  process.pid: 99261
  thread.id: 99261
---------------------------------------------------
Instrumentation: native: Function: 0x2d745e, File: python3.9
Instrumentation: native: Function: 0x3ab8f5, File: python3.9
Instrumentation: native: Function: 0x3ab350, File: python3.9
Instrumentation: native: Function: 0x3d5457, File: python3.9
Instrumentation: native: Function: 0x3d56ee, File: python3.9
Instrumentation: native: Function: 0x3a4095, File: python3.9
Instrumentation: native: Function: 0x27031e, File: python3.9
Instrumentation: cpython, Function: function_with_infinite_loop, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.9-scripts/eval.py, Line: 6, Column: 0
Instrumentation: cpython, Function: top_level_function, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.9-scripts/eval.py, Line: 10, Column: 0
Instrumentation: cpython, Function: <module>, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.9-scripts/eval.py, Line: 13, Column: 0
```

## fibonacci.py

```
------------------- New Sample --------------------
  thread.name: python
  process.executable.name: python3.9
  process.executable.path: /home/dpacak/.local/share/uv/python/cpython-3.9.23-linux-x86_64-gnu/bin/python3.9
  process.pid: 96757
  thread.id: 96757
---------------------------------------------------
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.9-scripts/fibonacci.py, Line: 8, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.9-scripts/fibonacci.py, Line: 8, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.9-scripts/fibonacci.py, Line: 8, Column: 0
Instrumentation: cpython, Function: recur_fibo, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.9-scripts/fibonacci.py, Line: 8, Column: 0
Instrumentation: cpython, Function: <module>, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.9-scripts/fibonacci.py, Line: 12, Column: 0
```