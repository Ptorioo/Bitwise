import uvloop
import logging
import asyncio
import time
from discord.ext import commands

uvloop.install()


class Music(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

        self._vc = {}
        self._is_paused = {}
        self._is_playing = {}
        self._musicQueue = {}
        self._queueIndex = {}
        self._duration = {}

    @property
    def vc(self):
        return self._vc

    @property
    def is_paused(self):
        return self._is_paused

    @property
    def is_playing(self):
        return self._is_playing

    @property
    def musicQueue(self):
        return self._musicQueue

    @property
    def queueIndex(self):
        return self._queueIndex

    @property
    def duration(self):
        return self._duration

    @vc.setter
    def vc(self, value):
        if isinstance(value, dict):
            self._vc = value
        else:
            raise ValueError("vc must be a dictionary")

    @is_paused.setter
    def is_paused(self, value):
        if isinstance(value, dict):
            self._is_paused = value
        else:
            raise ValueError("is_paused must be a dictionary")

    @is_playing.setter
    def is_playing(self, value):
        if isinstance(value, dict):
            self._is_playing = value
        else:
            raise ValueError("is_playing must be a dictionary")

    @musicQueue.setter
    def musicQueue(self, value):
        if isinstance(value, dict):
            self._musicQueue = value
        else:
            raise ValueError("musicQueue must be a dictionary")

    @queueIndex.setter
    def queueIndex(self, value):
        if isinstance(value, dict):
            self._queueIndex = value
        else:
            raise ValueError("queueIndex must be a dictionary")

    @duration.setter
    def duration(self, value):
        if isinstance(value, dict):
            self._duration = value
        else:
            raise ValueError("duration must be a dictionary")

    async def _init(self):
        for guild in self.bot.guilds:
            id = int(guild.id)
            self.vc[id] = None
            self.is_paused[id] = False
            self.is_playing[id] = False
            self.musicQueue[id] = []
            self.queueIndex[id] = 0
            self.duration[id] = []
        await self.on_time_update()

    async def _init_leave(self):
        for guild in self.bot.guilds:
            id = int(guild.id)
            if self.vc[id] != None:
                await self.vc[id].disconnect()
                self.vc[id] = None
            else:
                return

    async def on_time_update(self):
        while True:
            for guild in self.bot.guilds:
                id = int(guild.id)
                if not self.is_paused[id] and len(self.duration[id]) > 0:
                    self.duration[id][1] = time.time()
            await asyncio.sleep(1)

    @commands.Cog.listener()
    async def on_ready(self):
        await self._init()

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        id = int(guild.id)
        self.vc[id] = None
        self.is_paused[id] = False
        self.is_playing[id] = False
        self.musicQueue[id] = []
        self.queueIndex[id] = 0
        self.duration[id] = []
        logging.info(f"Music cog initialized from joining a new server! ID: {id}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        id = int(guild.id)
        self.vc[id] = None
        self.is_paused[id] = False
        self.is_playing[id] = False
        self.musicQueue[id] = []
        self.queueIndex[id] = 0
        self.duration[id] = []
        logging.info(f"Music cog reset from leaving a server! ID: {id}")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        id = int(member.guild.id)
        if not member.id == self.bot.user.id:
            return
        elif before.channel == None:
            if member.guild.me.guild_permissions.deafen_members:
                await member.edit(deafen=True)

            cooldownMinutes = 5
            time = 0

            while True:
                await asyncio.sleep(1)
                time += 1
                if self.is_playing[id] and not self.is_paused[id]:
                    time = 0
                if time >= cooldownMinutes * 60:
                    self.is_playing[id] = False
                    self.is_paused[id] = False
                    self.musicQueue[id] = []
                    self.queueIndex[id] = 0
                    self.duration[id] = []
                    await self.vc[id].disconnect()
                if self.vc[id] == None or not self.vc[id].is_connected():
                    break


async def setup(bot):
    await bot.add_cog(Music(bot))
