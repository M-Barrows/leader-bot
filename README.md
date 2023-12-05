Docker Container used to handle Slack Slash commands for Advent Of Code private leaderboards
In order to run, you will need to set the following container environment variables:

* AOC_COOKIE {This is just your session cookie value}
* AOC_LEADERBOARD_ID {This is the ID value for your private leaderboard}

The service is a FastAPI service that runs on port 80 in the container. 

Example run command: 
`docker run -d -e AOC_COOKIE=realylongsessionvaluegoeshere -e AOC_LEADERBOARD_ID=123456 -p 80:80 codecoffee/leader-bot:latest`

Limitations: 
* Hardcoded to 2023
* Only supports plaintext output for slack
* Only displayed for the requesting user, not the whole channel