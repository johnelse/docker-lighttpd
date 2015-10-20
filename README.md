docker-lighttpd
---------------

Run a lighttpd webserver in a docker container.

Build with `make`. This will create a docker image tagged as `$USER/lighttpd`.

This can be launched using docker directly; alternatively use `run.py` for
better checking of arguments, e.g.

```
./run.py --address 0.0.0.0 --port 1234 /myfiles
```

This will start a container serving up the `/myfiles` host directory, and will
forward the host address `0.0.0.0:1234` to the container's listening port (which
is always `8080`).
