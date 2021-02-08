# MiscDiscordBots
A repository of miscellaneous Discord bots that I make on whims.

# Organization
Each of the bots is given its own folder and a single master `.py` file to contain the entirety of its code.  It would not be difficult to create one general purpose bot for all of the different purposes that each bot serves, but I prefer this method of organization (I also like having a lot of different bots in my Discord test server.)

# The Bots
### Role Bot
This bot is configured with a preset list of roles and Discord message reactions to go along with each role.  When the bot is run, it sends a message to a pre-configured channel in your Discord server that allows users to assign themselves roles by reaction to this message.  Below is an example of what the message looks like when the bot is run.  When the bot is started subsequent times, it will delete its old message and resend the message again.

![Role Bot](https://i.imgur.com/becQGTN.png)

### Typing Bot
This bot takes a pre-configured bank of passages (found in test_bank.json) and allows users to take a simple typing test using the command `t!test` (this command must be sent to any of a list of pre-configured channels.)  An example of the bot working can be seen below.

![Typing Bot](https://i.imgur.com/v92tgKN.gif)
