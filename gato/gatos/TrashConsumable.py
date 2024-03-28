from random import randint

import discord
from discord.ext import commands

from discord.ext.commands.context import Context
from discord.ui import View

from AConsumable import AConsumable


class TrashConsumable(AConsumable):
    """> Poison food. Reduces HP by 20, restores 50 hunger."""

    # TODO: take the HSR trash image from some wiki and upload to imgbb.com
    IMAGE: str = "https://i.ibb.co/9n5gT9D/download.png"
    ANIMATIONS: str = "trash"
    DISPLAY_NAME: str = "Trash"
    RARITY: int = 3

    async def consume(self, ctx: Context, gatogame, gato = None):
        await super().consume(ctx, gatogame, gato)

        if gato is None:
            embed = discord.Embed(
                title = self.DISPLAY_NAME,
                description = "You need to specify a critter to use this on",
                colour = discord.Colour.red()
            )
            await ctx.send(embed=embed)
            return False

        if gato._fainted:
            embed = discord.Embed(
                title = self.DISPLAY_NAME,
                description = "This critter has fainted, please revive it first",
                colour = discord.Colour.red()
            )
            await ctx.send(embed=embed)
            return False

        gato.add_hunger(50)
        gato.add_health(-20)

        embed = discord.Embed(
            title = self.DISPLAY_NAME,
            description = f"**50 hunger** were restored to **{gato.name}** and it lost **20 HP**",
            colour = discord.Colour.teal()
        )
        await ctx.send(embed=embed)
        return True
