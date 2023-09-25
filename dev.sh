#!/bin/bash

# docker build -t prompt .
docker run -idt -p 3000:3000 -p 8000:8000 -v $PWD:/app --name prompt-dev prompt-eng /bin/bash

docker exec -it prompt-dev /bin/bash
