#!/bin/bash
# Get th size of the http.
curl -s "$1" | wc -c
