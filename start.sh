#!/usr/bin/env bash
exec gunicorn -w $WORKERS --access-logfile - -k gevent  -b 127.0.0.1:$PORT manager:app