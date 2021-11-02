
# TSSX

# Forked from tssx repo
[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](http://goldsborough.mit-license.org)


# Updates1: to make it work for python3 UNIX socket
# Updates2: to make it compile on gnu9.3
# Updates3: Update accept to accept4
# Updates4: change int type of buffer size to uint64_t
# Updates5: simple python code to test throughput ------> which shows 4x throughput comparing to original Unix domain socket.

# try this bench: https://github.com/goldsborough/ipc-bench


TSSX stands for *transparent shared-memory socket exchange* and is a system-level C library that silently replaces domain socket communication with a custom shared memory data channel, promising performance improvements up to an order of magnitude.

## Updated Usage for python

```shell
$ LD_PRELOAD=$PWD/path/to/libtssx-server.so python3 happy-banana-server.py
$ LD_PRELOAD=$PWD/path/to/libtssx-client.so python3 happy-banana-client.py
