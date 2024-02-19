#!/usr/bin/env bash


cd Python && uvicorn main:app --host 0.0.0.0 --port 8000 --reload

exec "$@"

