import discord
from discord.ext import commands
import pycord.wavelink as wavelink
import builder.queueBuilder as queue
import asyncio

class Voice(commands.Cog):
    def __init__(self, bot: discord.AutoShardedBot):
        self.bot = bot
        self.queue = queue.Queue()

    @commands.slash_command(name='play', description='This command plays a song!')
    async def play(self, ctx: discord.ApplicationContext, search: str):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')
        
        song = await wavelink.YouTubeTrack.search(query=search, return_first=True)

        if not song:
            return await ctx.respond('no song found!')
        
        await vc.play(song)
        
        emb = discord.Embed(
            title=f'Now playing {song.title}!',
            url=song.info["uri"],
            color=discord.Colour.red()
        )
        
        emb.add_field(name="Creator", value=song.info["author"], inline=True)
        emb.add_field(name="Duration", value=f'~{round(int(song.info["length"])/60000)}min', inline=True)
        
        
        await ctx.respond(embed=emb)
        
    @commands.slash_command(name='stop', description='This command stops the music!')
    async def stop(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not vc:
            return await ctx.respond('I am not connected to a voice channel!')

        await vc.stop()
        await ctx.respond('Stopped!')
        
    @commands.slash_command(name='pause', description='This command pauses the music!')
    async def pause(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not vc:
            return await ctx.respond('I am not connected to a voice channel!')

        await vc.pause()
        await ctx.respond('Paused!')
        
    @commands.slash_command(name='resume', description='This commands resumes the music!')
    async def resume(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not vc:
            return await ctx.respond('I am not connected to a voice channel!')

        await vc.resume()
        await ctx.respond('Resumed!')
        
    # queue commands
    @commands.slash_command(name='play_queue', description='This command plays the queue!')
    async def play_queue(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')
        
        song = self.queue.get_current_song()
        
        await vc.play(song)
        
        emb = discord.Embed(
            title=f'Now playing {song.title}!',
            url=song.info["uri"],
            color=discord.Colour.red()
        )
        
        emb.add_field(name="Creator", value=song.info["author"], inline=True)
        emb.add_field(name="Duration", value=f'~{round(int(song.info["length"])/60000)}min', inline=True)
        
        
        await ctx.respond(embed=emb)    

    @commands.slash_command(name='add_queue', description='This command adds a song to the queue!')
    async def add_queue(self, ctx: discord.ApplicationContext, search: str):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')

        song = await wavelink.YouTubeTrack.search(query=search, return_first=True)

        if not song:
            return await ctx.respond('no song found!')
        
        self.queue.add_song(song)
        
        emb = discord.Embed(
            title=f'Added {song.title} to the queue!',
            url=song.info["uri"],
            color=discord.Colour.red()
        )
        
        emb.add_field(name="Creator", value=song.info["author"], inline=True)
        emb.add_field(name="Duration", value=f'~{round(int(song.info["length"])/60000)}min', inline=True)
        
        await ctx.respond(embed=emb)
        
    @commands.slash_command(name='next', description='This command plays the next song in the queue!')
    async def next(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')
        
        song = self.queue.next_song()
        
        if not song:
            return await ctx.respond('no song found!')
        
        await vc.play(song)
        
        emb = discord.Embed(
            title=f'Now playing {song.title}!',
            url=song.info["uri"],
            color=discord.Colour.red()
        )
        
        emb.add_field(name="Creator", value=song.info["author"], inline=True)
        emb.add_field(name="Duration", value=f'~{round(int(song.info["length"])/60000)}min', inline=True)
        
        await ctx.respond(embed=emb)
        
    @commands.slash_command(name='previous', description='This command plays the previous song from the queue!')
    async def previous(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')
        
        song = self.queue.previous_song()
        
        if not song:
            return await ctx.respond('no song found!')
        
        await vc.play(song)
        
        emb = discord.Embed(
            title=f'Now playing {song.title}!',
            url=song.info["uri"],
            color=discord.Colour.red()
        )
        
        emb.add_field(name="Creator", value=song.info["author"], inline=True)
        emb.add_field(name="Duration", value=f'~{round(int(song.info["length"])/60000)}min', inline=True)
        
        await ctx.respond(embed=emb)
        
    @commands.slash_command(name='remove', description='This command removes the first instance of a song from!')
    async def remove(self, ctx: discord.ApplicationContext, search: str):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')
        
        song = await wavelink.YouTubeTrack.search(query=search, return_first=True)

        if not song:
            return await ctx.respond('no song found!')
        
        await self.queue.remove_song(song)
        
        emb = discord.Embed(
            title=f'Removed {song.title} from the queue!',
            url=song.info["uri"],
            color=discord.Colour.red()
        )
        
        emb.add_field(name="Creator", value=song.info["author"], inline=True)
        emb.add_field(name="Duration", value=f'~{round(int(song.info["length"])/60000)}min', inline=True)
        
        await ctx.respond(embed=emb)
        
    @commands.slash_command(name='clear_queue', description='This command clears the queue!')
    async def clear(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')
        
        await self.queue.clear()
        
        emb = discord.Embed(
            title=f'Cleared the queue!',
            color=discord.Colour.red()
        )
        
        await ctx.respond(embed=emb)
        
    @commands.slash_command(name='shuffle', description='This command shuffles the queue!')
    async def shuffle(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')
        
        song = self.queue.shuffle()
        
        await vc.play(song)
        
        emb = discord.Embed(
            title=f'Now playing {song.title}!',
            url=song.info["uri"],
            color=discord.Colour.red()
        )
        
        emb.add_field(name="Creator", value=song.info["author"], inline=True)
        emb.add_field(name="Duration", value=f'~{round(int(song.info["length"])/60000)}min', inline=True)
        
        
        await ctx.respond(embed=emb)

    @commands.slash_command(name='loop', description='This command loops the current song.')
    async def loop(self, ctx: discord.ApplicationContext, search: str):
        vc = ctx.voice_client

        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond('You must be in the same voice channel as the bot!')
        
        song = await wavelink.YouTubeTrack.search(query=search, return_first=True)

        if not song:
            return await ctx.respond('no song found!')
        
        emb = discord.Embed(
            title=f'Now playing `{song.title}` on loop!',
            url=song.info["uri"],
            color=discord.Colour.red()
        )
        
        emb.add_field(name="Creator", value=song.info["author"], inline=True)
        emb.add_field(name="Duration", value=f'~{round(int(song.info["length"])/60000)}min', inline=True)

        while True:
            if not vc.is_playing():
                await vc.play(song)
            await asyncio.sleep(song.duration//1000)

def setup(bot):
    bot.add_cog(Voice(bot))