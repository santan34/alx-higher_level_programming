#!/bin/bash
#sends a request to a URL
curl -Is "$1" | grep -i Content-Length | awk '{print $2}' 
