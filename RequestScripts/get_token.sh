#!/bin/bash

# Get token for a user

read -p "Username : " username
read -s -p "Password : " pswd
data="{\"username\":\"${username}\", \"password\":\"${pswd}\"}"

echo
curl -X POST -H 'Content-Type: application/json' -d "${data}" localhost:8000/api/auth-token/ 
echo


