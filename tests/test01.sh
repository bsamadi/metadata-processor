#!/bin/bash

curl localhost:5000/detect_glare -X POST -d '{"lat": 49.2699648, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2}' -H 'Content-Type: application/json'
