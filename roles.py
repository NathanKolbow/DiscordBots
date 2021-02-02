import discord

GUILD_ID = 803468061624893442
CHANNEL_ID = 803470578366677053

ROLE_DICT = {
    '🎮': 803470803936870400,
    '♟️': 803476500501495819,
    '🍓': 803476868275503104,
    '👺': 803476956254961693,
    '⌨️': 806206997137326121
}
ROLE_DESCRIPTIONS = {
    '🎮': 'Oppressed Citizen',
    '♟️': 'Chess',
    '🍓': 'Fruit Lover',
    '👺': 'Scary Demon',
    '⌨️': 'Keyboard Kutie'
}


class Client(discord.Client):
    async def on_ready(self):
        global ENFORCED_ROLE

        print('Logged on as', self.user)
        channel = client.get_channel(CHANNEL_ID)
        await channel.purge(limit=5, check=is_me)
        
        # Build the message
        msg_content = "**I only work if I am listed as online in the right-hand panel.  React with any of the following icons to receive the corresponding roll.**\n\n"
        for key in ROLE_DESCRIPTIONS:
            msg_content += key + ': ' + ROLE_DESCRIPTIONS[key] + '\n'
        
        msg = await channel.send(content=msg_content)
        
        guild = client.get_guild(GUILD_ID)
        for reaction in ROLE_DICT:
            ROLE_DICT[reaction] = guild.get_role(ROLE_DICT[reaction])
            await msg.add_reaction(reaction)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

    async def on_reaction_add(self, reaction, user):
        if reaction.emoji not in ROLE_DICT:
            await reaction.message.remove_reaction(reaction.emoji, user)
            return

        if user == self.user:
            return

        await user.add_roles(ROLE_DICT[reaction.emoji])


def is_me(m):
    return m.author == client.user


client = Client()
client.run('MzUwMTQyOTY0MzU5NzU3ODI1.WZ5eDA.r-RmUYRvf4CEmUbP7TeMt6YzCgM')
