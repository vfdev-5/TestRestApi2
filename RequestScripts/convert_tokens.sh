#!/usr/bin/env bash

client_id='ElrT1m4zzwpQIMMUtGtvv0hktkkfT5kvPsQDxLk3'
client_secret='mBOuU9ckri87tTDRl8eZvJcIYRAiP9I4ifYwxwQLTPhblR3iArC9rfqr39YMcjF9vgZIWfy6ldUvomk0Ma3y5DjMIsxdd1Ik3w9quLdn1TkGDW4xDcqOVBEoFWMhmz5I'

backend='github'
social_token=''

curl -X POST -d "grant_type=convert_token&client_id=${client_id}&client_secret=${client_secret}&backend=${backend}&token=${social_token}" http://localhost:8000/auth/convert-token
echo