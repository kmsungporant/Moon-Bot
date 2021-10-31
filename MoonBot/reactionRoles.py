import nextcord
import config
from nextcord.ext import commands



class reactionRoles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def roles(self, ctx):
        embed = nextcord.Embed(title = "Role Selection | Moon Bot", description = "Click on the emojis to add/remove roles!\n")
        embed.add_field(name = "__Nations__", value = "Fire Benders 🔥\nAir Benders 💨\nEarth Benders 🪨\nWater Benders 🌊")
        embed.add_field(name = "__other__", value = "Pokemon Go 🔴")
        msg = await ctx.send(embed=embed)
        self.messageId = msg.id
        await msg.add_reaction("🔥")
        await msg.add_reaction("💨")
        await msg.add_reaction("🪨")
        await msg.add_reaction("🌊")
        await msg.add_reaction("🔴")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id == self.client.user.id:
            return
        if reaction.emoji == "🔥":
            role = nextcord.utils.get(user.guild.roles, name="Fire Benders 🔥")
        elif reaction.emoji == "💨":
            role = nextcord.utils.get(user.guild.roles, name="Air Benders 💨")
        elif reaction.emoji == "🪨":
            role = nextcord.utils.get(user.guild.roles, name="Earth Benders 🪨")
        elif reaction.emoji == "🌊":
            role = nextcord.utils.get(user.guild.roles, name="Water Benders 🌊")
        elif reaction.emoji == "🔴":
            role = nextcord.utils.get(user.guild.roles, name="Pokemon Go 🔴")
        if nextcord.utils.get(user.roles, name=role.name):
            await user.remove_roles(role)
        else:
            if role.name == "Fire Benders 🔥" or role.name == "Air Benders 💨" or role.name == "Earth Benders 🪨" or role.name == "Water Benders 🌊":
                await self.reactRoles(user)
            await user.add_roles(role)
        await reaction.remove(user)
            
    async def reactRoles(self, user):
        for role in user.roles:
            if role.name == "Fire Benders 🔥" or role.name == "Air Benders 💨" or role.name == "Earth Benders 🪨" or role.name == "Water Benders 🌊":
                await user.remove_roles(role)
    
        

def setup(client):
    client.add_cog(reactionRoles(client))