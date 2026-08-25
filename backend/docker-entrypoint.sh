#!/bin/bash
python -m scripts.main
exec "fastapi" "dev" "--port" "80" "--host" "0.0.0.0"
