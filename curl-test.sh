#!/bin/bash

curl --request GET http://localhost:5001/api/timeline_post

curl --request POST http://localhost:5001/api/timeline_post -d 'name=Amar&email=ask20@rice.edu&content=Writing Automated Tests using curl'

curl --request GET http://localhost:5001/api/timeline_post
