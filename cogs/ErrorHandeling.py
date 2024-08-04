from discord.ext import commands

class ErrorHandeling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f"An error occurred: {str(error)}")
async def setup(bot):
    await bot.add_cog(ErrorHandeling(bot))
