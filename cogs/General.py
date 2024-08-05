import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(description='Show you the Devleloper')
    async def developer(self, ctx: commands.Context):
        embed = discord.Embed(
            description=f"**My Devloper\n\n**maxiroe\n\n\n",
            colour=0x0000FF
        )
        embed.set_footer(text=f"requestet by: {ctx.author}")
        if not ctx.interaction:
            await ctx.send(embed=embed)
            await ctx.message.delete()
        else:
            await ctx.interaction.response.send_message(embed=embed)

    @commands.hybrid_command(description='Show you Informations about the Bot')
    async def botinfo(self, ctx):
        embed = discord.Embed(title='Bot-Informations', colour=0x0000FF)
        embed.add_field(name='Botname', value=f'{self.bot.name}', inline=False)
        embed.add_field(name='Botversion', value='b.1.0.0', inline=False)
        embed.add_field(name='Botdeveloper', value=f'maxiroe', inline=False)
        embed.add_field(name='Botdescription', value=f'Hey i am a example tutorial Bot feel free to use this as an example.', inline=False)
        embed.add_field(name='Support', value=f'If you have any issues you can DM me on discord my username is maxiroe')
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
