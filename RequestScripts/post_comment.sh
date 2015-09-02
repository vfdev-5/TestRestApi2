#!/bin/bash

# Post a comment by user

data="{\"comment\":\"This is another test comment created by a user : vfdev\"}"

echo
curl -X POST -H 'Content-Type: application/json' -d "${data}" localhost:8000/api/comment/ -H 'Authorization: Token '
echo


