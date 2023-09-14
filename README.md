# AI-Contest-CPATS
Docker Instructions

docker build -t ai-contest .
docker run --mount type=bind,source="%cd%\questions",target=/app/questions --mount type=bind,source="%cd%\solutions",target=/app/solutions -it ai-contest bash
 
%cd% - can be the location of any question

The game server will execute: (aka do it in the interactive bash console after run)

bash ./main.sh "evalmessage"
