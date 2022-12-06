#!/bin/bash

cd src
flask run

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]]; 
  do sleep 1; 
done

poetry run robot tests

status=$?

kill $(lsof -t -i:5000)

exit $status