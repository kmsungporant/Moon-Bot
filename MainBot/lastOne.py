import nextcord
import json
import time
from nextcord.ext import commands, tasks

class lastOne(commands.Cog):
    def __init__(self,client):
        self.client = client


    
            
        
def setup(client):
    client.add_cog(lastOne(client))