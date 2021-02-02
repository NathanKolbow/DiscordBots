import discord
from time import time
import Levenshtein as lev
import json

AUTHORIZED_CHANNELS = [ 806189740310790154 ]

CURR_TEST = 0
TEST_BANK = None
RUNNING_TESTS = {}

class Client(discord.Client):
    async def on_ready(self):
        global TEST_BANK
        with open('test_bank.json', 'r') as f:
            TEST_BANK = json.loads(f.read())
    
        print('Logged on as', self.user)
        
        # Uncomment the following line to clear the given channel's messages when the bot logs on
        # await client.get_channel(AUTHORIZED_CHANNELS[0]).purge()

    async def on_message(self, message):
        global CURR_TEST
        global TEST_BANK
        global RUNNING_TESTS
        
        # don't respond to ourselves
        if message.author == self.user:
            return
            
        if message.channel.id not in AUTHORIZED_CHANNELS:
            return

        if message.author in RUNNING_TESTS:
            await score_response(message)
            return

        if message.content == 't!test':
            await message.delete()
            test = TEST_BANK[CURR_TEST]
            embed = discord.Embed(title=test['title'] + ' by ' + test['credit'], description=test['text'], color=0xff0000)
            # embed.add_field(name="", value=message.author, inline=True)
            msg = await message.channel.send(content=message.author.mention, embed=embed)
            
            RUNNING_TESTS[message.author] = {
                'test' : TEST_BANK[CURR_TEST],
                'start': time(),
                'msg'  : msg,
                'embed': embed
            }
            CURR_TEST = (CURR_TEST + 1) % len(TEST_BANK)
        elif message.content == 't!info':
            await message.delete()
            embed = discord.Embed(title='t!info', color=0xffb6c1, description='I am a bot that provides typing tests via the `t!test` command. WPM (words per minute) is calculated with the standard 1 word = 5 characters typed (as opposed to the actual number of words typed in a given passage) and accuracy is calculated via an adjusted [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance).')
            embed.set_thumbnail(url=self.user.avatar_url)
            await message.channel.send(content=message.author.mention, embed=embed)


# Returns speed, acc for user using stored data in RUNNING_TESTS
async def score_response(message):
    global RUNNING_TESTS
    
    run_time = time() - RUNNING_TESTS[message.author]['start']

    acc = max(0, (1 - (lev.distance(RUNNING_TESTS[message.author]['test']['text'], message.content) / len(message.content))) * 100)
    speed = (len(message.content) / 5) / (run_time / 60)
    aWPM = max(0, speed * (((acc/100) ** 2) * (acc/100)))

    await message.delete()
    new_embed = RUNNING_TESTS[message.author]['embed']
    new_embed.description = new_embed.description + '\n*' + message.content + '*'
    new_embed.color = 0x00ff00
    new_embed.add_field(name=message.author, value="%.2f WPM @ %.2f%% accuracy\n%.2f aWPM" % (speed, acc, aWPM))
    new_embed.set_thumbnail(url=message.author.avatar_url)
    await RUNNING_TESTS[message.author]['msg'].edit(content="", embed=new_embed)
    del RUNNING_TESTS[message.author]


def is_me(m):
    return m.author == client.user


client = Client()
with open('typing_test.secret', 'r') as f:
    secret = f.read()

client.run(secret)
