#!/usr/bin/env bash

client_id='7Ws5WFKJvFuz57BMHPQIB86CHh57fXpw072JyNvz'
client_secret='TTCuyx7Ck8Lu0LL4UeYgWmrIC75YCf26PEJJvo0SThUhkhVjQNmu4LEDQ34mAj885WkaNZ2mZqdrga3Gfz9mEN66o9Y8QCw5nbLY5TWSk0T7SxZDYMv2YbKNyyBtXsps'

backend='github'
social_token='c3aa642377182bc0b537c95da282c1ccf05b6915'

curl -X POST -d "grant_type=convert_token&client_id=${client_id}&client_secret=${client_secret}&backend=${backend}&token=${social_token}" http://localhost:8000/api/auth/convert-token > log.html
echo