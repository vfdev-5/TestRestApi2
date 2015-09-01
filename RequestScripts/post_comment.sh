#!/bin/bash

# Post a comment by user

data="{\"comment\":\"This is another test comment created by a user : vfdev\"}"

echo
curl -X POST -H 'Content-Type: application/json' -d "${data}" localhost:8000/api/comment/ -H 'Authorization: Token 20bc9187c436e47ce7d2caa7f896a40dd91782ee'
echo


