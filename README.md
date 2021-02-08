# The Bots
### Typing Bot
This bot takes a pre-configured bank of passages (found in test_bank.json) and allows users to take a simple typing test using the command `t!test` (this command must be sent to any of a list of pre-configured channels.)  An example of the bot working can be seen below.

![Typing Bot](https://i.imgur.com/v92tgKN.gif)

### Role Bot
This bot is configured with a preset list of roles and Discord message reactions to go along with each role.  When the bot is run, it sends a message to a pre-configured channel in your Discord server that allows users to assign themselves roles by reaction to this message.  Below is an example of what the message looks like when the bot is run.  When the bot is started subsequent times, it will delete its old message and resend the message again.

![Role Bot](https://i.imgur.com/becQGTN.png)

# Organization
Each of the bots is given its own folder, a single master `.py` file to contain the entirety of its code, and its own `bot.secret` file containing the bot's secret token.  It would not be difficult to create one general purpose bot that amalgamates the functionality of each individual bot, but I prefer this method of organization (I also like having a lot of different bots in my Discord test server.)  This organizational format also makes life much easier for anyone looking to learn from any single bot's source code.

# Credit
As per the `LICENSE` all of the code in this repo is free to use for any purpose without promise of any warranty or liability from myself.  I only ask that if you do adapt the source code from any of these bots that you credit me wherever you feel appropriate.
