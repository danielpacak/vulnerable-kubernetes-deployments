# React SSR with Express, Webpack, and Babel

https://www.youtube.com/watch?v=LRohAW0WYZM

```
npm install && npm start
```

Navigate to http://localhost:3001

## Docker

```
docker build \
  --build-arg NODE_VERSION=20.10.0 \
  --build-arg BASE_IMAGE=alpine \
  --tag docker.io/danielpacak/react-ssr-with-express:node20.10.0-alpine .
```

```
docker build \
  --build-arg NODE_VERSION=20.10.0 \
  --build-arg BASE_IMAGE=bullseye-slim \
  --tag docker.io/danielpacak/react-ssr-with-express:node20.10.0-bullseye-slim .
```

```
docker run -d --rm --name react-ssr-with-express -p 3001:3001 docker.io/danielpacak/react-ssr-with-express:node20.10.0-alpine
```

```
IMAGE_TAR=/tmp/react-ssr-with-express.tar
docker image save -o $IMAGE_TAR docker.io/danielpacak/react-ssr-with-express
sudo ctr -n k8s.io image import $IMAGE_TAR && rm $IMAGE_TAR
```

```
sudo ctr -n k8s.io image ls | grep react
```

## Kubernetes

```
k apply -f react-ssr-with-express.kubernetes.yaml
```

```
k port-forward -n react-ssr-with-express svc/react-ssr-with-express 3001:3001
```

## Notes

Install and port forward with `vkd` CLI.

```
vkd install react-ssr-with-express
```

## Event-Based Stack Traces

### Mode: Development

```
--------------- New Resource Profile --------------
  container.id: c320772527bd687ce9d47e396f02625921cf2ef5dd42e933832fc689c67454f7 (Str)
  k8s.pod.name: react-ssr-with-express-58b47f94f4-5kfpg (Str)
  k8s.namespace.name: react-ssr-with-express (Str)
  k8s.pod.uid: 376a8e89-4412-4cac-8eec-51c200066fd5 (Str)
  k8s.deployment.name: react-ssr-with-express (Str)
  k8s.node.name: kube-control-plane (Str)
  k8s.cluster.uid: 55383944-1970-45b5-a24e-ae178dc09578 (Str)
  k8s.container.name: react-ssr-with-express (Str)
  container.image.name: docker.io/danielpacak/react-ssr-with-express (Str)
  container.image.tag: node20.10.0-bullseye-slim (Str)
------------------- New Profile -------------------
  ProfileID: 00000000000000000000000000000000
  Time: 2025-12-08 11:51:41.134432707 +0000 UTC
  Duration: 0 ns
  Period: 0
  PeriodType: [, ]
  Dropped attributes count: 0
  SampleType: events
------------------- New Sample --------------------
  timestamp[0]: 2025-12-08 11:51:43.865055543 +0000 UTC (1765194703865055543)
  timestamp[1]: 2025-12-08 11:51:44.073635072 +0000 UTC (1765194704073635072)
  thread.name: node (Str)
  process.executable.name: node (Str)
  process.executable.path: /usr/local/bin/node (Str)
  process.pid: 69586 (Int)
  thread.id: 69586 (Int)
  cpu.logical_number: 3 (Int)
---------------------------------------------------
  kernel: Function: copy_process, File: , Line: 0, Column: 0
  kernel: Function: __do_sys_clone, File: , Line: 0, Column: 0
  kernel: Function: __x64_sys_clone, File: , Line: 0, Column: 0
  kernel: Function: x64_sys_call, File: , Line: 0, Column: 0
  kernel: Function: do_syscall_64, File: , Line: 0, Column: 0
  kernel: Function: entry_SYSCALL_64_after_hwframe, File: , Line: 0, Column: 0
  native: Function: 0xc79fa, File: libc-2.31.so
  native: Function: 0x188cb3b, File: node
  native: Function: 0xdab0cf, File: node
  native: Function: 0xf29f4e, File: node
  native: Function: 0xf2a7bc, File: node
  native: Function: 0xf2ac84, File: node
  v8js: Function: V8::BuiltinExitFrame, File: , Line: 0, Column: 0
  v8js: Function: ChildProcess.spawn, File: node:internal/child_process, Line: 0, Column: 0
  v8js: Function: spawn, File: node:child_process, Line: 0, Column: 0
  v8js: Function: <anonymous>, File: node:child_process, Line: 0, Column: 0
  v8js: Function: exec, File: node:child_process, Line: 0, Column: 0
  v8js: Function: <anonymous>, File: , Line: 100, Column: 0
  v8js: Function: handleRequest, File: , Line: 152, Column: 0
  v8js: Function: next, File: , Line: 160, Column: 0
  v8js: Function: <anonymous>, File: , Line: 117, Column: 0
  v8js: Function: handle, File: , Line: 435, Column: 0
  v8js: Function: handleRequest, File: , Line: 152, Column: 0
  v8js: Function: <anonymous>, File: , Line: 295, Column: 0
  v8js: Function: <anonymous>, File: , Line: 582, Column: 0
  v8js: Function: next, File: , Line: 291, Column: 0
  v8js: Function: <anonymous>, File: , Line: 186, Column: 0
  v8js: Function: handle, File: , Line: 177, Column: 0
  v8js: Function: app, File: , Line: 38, Column: 0
  v8js: Function: emit, File: node:events, Line: 0, Column: 0
  v8js: Function: parserOnIncoming, File: node:_http_server, Line: 1146, Column: 0
  v8js: Function: parserOnHeadersComplete, File: node:_http_common, Line: 0, Column: 0
  v8js: Function: V8::InternalFrame, File: , Line: 0, Column: 0
  v8js: Function: V8::EntryFrame, File: , Line: 0, Column: 0
  native: Function: 0x10223ca, File: node
  native: Function: 0x1023463, File: node
  native: Function: 0xee58dc, File: node
  native: Function: 0xcc4e16, File: node
  native: Function: 0xcc51a5, File: node
  native: Function: 0x1ed1bf1, File: node
  native: Function: 0xcc3da2, File: node
  native: Function: 0xcc55c2, File: node
  native: Function: 0xdb8671, File: node
  native: Function: 0xdb8a96, File: node
  native: Function: 0x188f44c, File: node
  native: Function: 0x188f7df, File: node
  native: Function: 0x18971ba, File: node
  native: Function: 0x1883516, File: node
  native: Function: 0xbb5b82, File: node
  native: Function: 0xced014, File: node
  native: Function: 0xced9dc, File: node
  native: Function: 0xc588a6, File: node
  native: Function: 0x23d09, File: libc-2.31.so
  native: Function: 0xbb2afd, File: node
------------------- End Sample --------------------
------------------- New Sample --------------------
  timestamp[0]: 2025-12-08 11:51:41.134432707 +0000 UTC (1765194701134432707)
  timestamp[1]: 2025-12-08 11:51:42.62019265 +0000 UTC (1765194702620192650)
  timestamp[2]: 2025-12-08 11:51:42.904901326 +0000 UTC (1765194702904901326)
  timestamp[3]: 2025-12-08 11:51:43.068187917 +0000 UTC (1765194703068187917)
  timestamp[4]: 2025-12-08 11:51:43.203762875 +0000 UTC (1765194703203762875)
  timestamp[5]: 2025-12-08 11:51:43.446192266 +0000 UTC (1765194703446192266)
  timestamp[6]: 2025-12-08 11:51:43.61001597 +0000 UTC (1765194703610015970)
  thread.name: node (Str)
  process.executable.name: node (Str)
  process.executable.path: /usr/local/bin/node (Str)
  process.pid: 69586 (Int)
  thread.id: 69586 (Int)
  cpu.logical_number: 2 (Int)
---------------------------------------------------
  kernel: Function: copy_process, File: , Line: 0, Column: 0
  kernel: Function: __do_sys_clone, File: , Line: 0, Column: 0
  kernel: Function: __x64_sys_clone, File: , Line: 0, Column: 0
  kernel: Function: x64_sys_call, File: , Line: 0, Column: 0
  kernel: Function: do_syscall_64, File: , Line: 0, Column: 0
  kernel: Function: entry_SYSCALL_64_after_hwframe, File: , Line: 0, Column: 0
  native: Function: 0xc79fa, File: libc-2.31.so
  native: Function: 0x188cb3b, File: node
  native: Function: 0xdab0cf, File: node
  native: Function: 0xf29f4e, File: node
  native: Function: 0xf2a7bc, File: node
  native: Function: 0xf2ac84, File: node
  v8js: Function: V8::BuiltinExitFrame, File: , Line: 0, Column: 0
  v8js: Function: ChildProcess.spawn, File: node:internal/child_process, Line: 0, Column: 0
  v8js: Function: spawn, File: node:child_process, Line: 0, Column: 0
  v8js: Function: <anonymous>, File: node:child_process, Line: 0, Column: 0
  v8js: Function: exec, File: node:child_process, Line: 0, Column: 0
  v8js: Function: <anonymous>, File: , Line: 100, Column: 0
  v8js: Function: handleRequest, File: , Line: 152, Column: 0
  v8js: Function: next, File: , Line: 160, Column: 0
  v8js: Function: <anonymous>, File: , Line: 117, Column: 0
  v8js: Function: handle, File: , Line: 435, Column: 0
  v8js: Function: handleRequest, File: , Line: 152, Column: 0
  v8js: Function: <anonymous>, File: , Line: 295, Column: 0
  v8js: Function: <anonymous>, File: , Line: 582, Column: 0
  v8js: Function: next, File: , Line: 291, Column: 0
  v8js: Function: <anonymous>, File: , Line: 186, Column: 0
  v8js: Function: handle, File: , Line: 177, Column: 0
  v8js: Function: app, File: , Line: 38, Column: 0
  v8js: Function: emit, File: node:events, Line: 0, Column: 0
  v8js: Function: parserOnIncoming, File: node:_http_server, Line: 1146, Column: 0
  v8js: Function: parserOnHeadersComplete, File: node:_http_common, Line: 0, Column: 0
  v8js: Function: V8::InternalFrame, File: , Line: 0, Column: 0
  v8js: Function: V8::EntryFrame, File: , Line: 0, Column: 0
  native: Function: 0x10223ca, File: node
  native: Function: 0x1023463, File: node
  native: Function: 0xee58dc, File: node
  native: Function: 0xcc4e16, File: node
  native: Function: 0xcc51a5, File: node
  native: Function: 0x1ed1bf1, File: node
  native: Function: 0xcc3da2, File: node
  native: Function: 0xcc55c2, File: node
  native: Function: 0xdb8671, File: node
  native: Function: 0xdb8a96, File: node
  native: Function: 0x188f44c, File: node
  native: Function: 0x188f7df, File: node
  native: Function: 0x18971ba, File: node
  native: Function: 0x1883516, File: node
  native: Function: 0xbb5b82, File: node
  native: Function: 0xced014, File: node
  native: Function: 0xced9dc, File: node
  native: Function: 0xc588a6, File: node
  native: Function: 0x23d09, File: libc-2.31.so
  native: Function: 0xbb2afd, File: node
------------------- End Sample --------------------
------------------- End Profile -------------------
-------------- End Resource Profile ---------------
```

### Mode: Production

```
--------------- New Resource Profile --------------
  container.id: 9f972201b8b33944f00d2911494eb1968f91cdfef613a38bb9f75dafe7e85142 (Str)
  k8s.cluster.uid: 55383944-1970-45b5-a24e-ae178dc09578 (Str)
  k8s.pod.name: react-ssr-with-express-58b47f94f4-s2wsq (Str)
  k8s.namespace.name: react-ssr-with-express (Str)
  k8s.pod.uid: bb835cdf-b94f-4a3c-8059-b87fd7edf2d9 (Str)
  k8s.deployment.name: react-ssr-with-express (Str)
  k8s.node.name: kube-control-plane (Str)
  k8s.container.name: react-ssr-with-express (Str)
  container.image.name: docker.io/danielpacak/react-ssr-with-express (Str)
  container.image.tag: node20.10.0-bullseye-slim (Str)
------------------- New Profile -------------------
  ProfileID: 00000000000000000000000000000000
  Time: 2025-12-08 12:27:21.28725021 +0000 UTC
  Duration: 0 ns
  Period: 0
  PeriodType: [, ]
  Dropped attributes count: 0
  SampleType: events
------------------- New Sample --------------------
  timestamp[0]: 2025-12-08 12:27:21.28725021 +0000 UTC (1765196841287250210)
  thread.name: node (Str)
  process.executable.name: node (Str)
  process.executable.path: /usr/local/bin/node (Str)
  process.pid: 130480 (Int)
  thread.id: 130480 (Int)
  cpu.logical_number: 5 (Int)
---------------------------------------------------
  kernel: Function: copy_process, File: , Line: 0, Column: 0
  kernel: Function: __do_sys_clone, File: , Line: 0, Column: 0
  kernel: Function: __x64_sys_clone, File: , Line: 0, Column: 0
  kernel: Function: x64_sys_call, File: , Line: 0, Column: 0
  kernel: Function: do_syscall_64, File: , Line: 0, Column: 0
  kernel: Function: entry_SYSCALL_64_after_hwframe, File: , Line: 0, Column: 0
  native: Function: 0xc79fa, File: libc-2.31.so
  native: Function: 0x188cb3b, File: node
  native: Function: 0xdab0cf, File: node
  native: Function: 0xf29f4e, File: node
  native: Function: 0xf2a7bc, File: node
  native: Function: 0xf2ac84, File: node
  v8js: Function: V8::BuiltinExitFrame, File: , Line: 0, Column: 0
  v8js: Function: ChildProcess.spawn, File: node:internal/child_process, Line: 0, Column: 0
  v8js: Function: spawn, File: node:child_process, Line: 0, Column: 0
  v8js: Function: <anonymous>, File: node:child_process, Line: 0, Column: 0
  v8js: Function: exec, File: node:child_process, Line: 0, Column: 0
  v8js: Function: <anonymous>, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: p.handleRequest, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: r, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: <anonymous>, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: <anonymous>, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: p.handleRequest, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: <anonymous>, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: <anonymous>, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: k, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: <anonymous>, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: x.handle, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: e, File: /usr/src/app/dist/server.cjs, Line: 2, Column: 0
  v8js: Function: emit, File: node:events, Line: 0, Column: 0
  v8js: Function: parserOnIncoming, File: node:_http_server, Line: 0, Column: 0
  v8js: Function: parserOnHeadersComplete, File: node:_http_common, Line: 0, Column: 0
  v8js: Function: V8::InternalFrame, File: , Line: 0, Column: 0
  v8js: Function: V8::EntryFrame, File: , Line: 0, Column: 0
  native: Function: 0x10223ca, File: node
  native: Function: 0x1023463, File: node
  native: Function: 0xee58dc, File: node
  native: Function: 0xcc4e16, File: node
  native: Function: 0xcc51a5, File: node
  native: Function: 0x1ed1bf1, File: node
  native: Function: 0xcc3da2, File: node
  native: Function: 0xcc55c2, File: node
  native: Function: 0xdb8671, File: node
  native: Function: 0xdb8a96, File: node
  native: Function: 0x188f44c, File: node
  native: Function: 0x188f7df, File: node
  native: Function: 0x18971ba, File: node
  native: Function: 0x1883516, File: node
  native: Function: 0xbb5b82, File: node
  native: Function: 0xced014, File: node
  native: Function: 0xced9dc, File: node
  native: Function: 0xc588a6, File: node
  native: Function: 0x23d09, File: libc-2.31.so
  native: Function: 0xbb2afd, File: node
------------------- End Sample --------------------
------------------- End Profile -------------------
-------------- End Resource Profile ---------------
```

## TODO

1. Generate source maps with webpack and see if we can apply them to symbolized stack frames.
2. Build container images for development and production mode (to compare stack trace symbols).
3. Use Pyroscope SDK for Node.
4. Use Pyroscope SDK for Node with source maps.
