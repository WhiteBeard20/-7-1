import discord
from discord.ext import commands
from options import TOKEN
from cl_model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$',  
                   intents=intents,
                   help_command=None)

@bot.command()
async def photo(ctx):
    if ctx.message.attachments:
        for image in ctx.message.attachments:
            file_name = image.filename
            await image.save(f'./images/{file_name}')
            await ctx.send(f'Сохранил картинку в /images/{file_name}')
            await ctx.send(get_class(model_path='model/keras_model.h5', labels_path='model/labels.txt', image_path=f'images/{file_name}'))
    else:
        await ctx.send('Вы забыли загрузить картинку')

bot.run(TOKEN)
