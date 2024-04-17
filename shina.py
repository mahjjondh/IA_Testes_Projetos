import discord
from discord.ext import commands
import requests
from transformers import AutoTokenizer
from huggingface_hub import InferenceClient

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)
cl = discord.Client(intents=intents)

modelo = "stabilityai/stable-diffusion-xl-base-1.0"
modelo_txt = "mistralai/Mixtral-8x7B-Instruct-v0.1"
url = f'https://api-inference.huggingface.co/models/{modelo}'
urltexto = f'https://api-inference.huggingface.co/models/{modelo_txt}'

token = "SEU_TOKEN_DO_HF"
headers = {"Authorization": f"Bearer {token}"}

@bot.command()
async def misterious(ctx, prompt):
    try:
        client = InferenceClient(model="MysteriousAI/NSFW-gen", headers=headers)
        imagem = client.text_to_image(prompt)
        imagem.save("imagem.png")
        await ctx.send(file=discord.File('imagem.png'))
    except Exception as e:
        await ctx.send("Os meus servidores estão sobrecarregados, tente novamente mais tarde.")

@bot.command()
async def dalle3(ctx, prompt):
    try:
        client = InferenceClient(model="ehristoforu/dalle-3-xl-v2", headers=headers)
        imagem = client.text_to_image(prompt)
        imagem.save("imagem.png")
        await ctx.send(file=discord.File('imagem.png'))
    except Exception as e:
        await ctx.send("Os meus servidores estão sobrecarregados, tente novamente mais tarde.")

@bot.command()
async def stbl(ctx, prompt):
    try:
        client = InferenceClient(model="stabilityai/stable-diffusion-xl-base-1.0")
        imagem = client.text_to_image(prompt)
        imagem.save("imagem.png")
        #await ctx.send(prompt)
        await ctx.send(file=discord.File('imagem.png'))
    except Exception as e:
        await ctx.send("Os meus servidores estão sobrecarregados, tente novamente mais tarde.")

@bot.command()
async def shina(ctx, prompt):
    try:
        chat = [{"role": "user", "content": prompt}]

        tokenizer_mixtral = AutoTokenizer.from_pretrained(modelo_txt)
        template_mixtral = tokenizer_mixtral.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
        json = {
            "inputs": template_mixtral,
            "parameters": {"max_new_tokens": 250},
            "options": {'use_cache':False, 'wait_for_model':True}
        }
        response = requests.post(urltexto, json=json, headers=headers).json()
        mensagem = response[0]['generated_text'].split("[/INST]")[-1]
        await ctx.send(mensagem)
    except Exception as e:
        await ctx.send("Os meus servidores estão sobrecarregados, tente novamente mais tarde.")

@cl.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dm_channel = await member.create_dm()
    await dm_channel.send(f'Olá {member.name}, bem vindo ao servidor {guildname}! Eu sou a Shina, a assistente virtual do servidor. Se precisar de ajuda, é só me chamar! :D, para ver meus comandos digite !help_shina')

@bot.command()
async def simple_pool(ctx,title):
    MyEmbed = discord.Embed(title=title, color=discord.Color.dark_purple())
    message = await ctx.send(embed=MyEmbed)
    await message.add_reaction("👍")
    await message.add_reaction("👎")   


@bot.command()
async def help_shina(ctx):
    MyEmbed = discord.Embed(title="Comandos disponíveis", description="Esses são os meus comandos: ", color=discord.Color.dark_purple())
    MyEmbed.add_field(name='!shina "texto"', value="Fale comigo! eu ainda não tenho memoria então se eu esquecer me desculpe :)", inline=False)
    MyEmbed.add_field(name='!stbl "texto"', value="Cria uma imagem usando engine stability ai :)", inline=False)
    MyEmbed.add_field(name='!misterious "texto"', value="Cria uma imagem sem censura :O", inline=False)
    MyEmbed.add_field(name='!dalle3 "texto"', value="Cria uma imagem usando Dall-e 3 :)", inline=False)
    MyEmbed.add_field(name=';bonus_deck', value="Receba uma carta do baralho de aventura via pm!", inline=False)
    await ctx.send(embed=MyEmbed)
bot.run('TOKEN DO SEU BOT DO DISCORD')
