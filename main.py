# インストールした discord.py を読み込む
import discord

TOKEN = "NTUyMDkzNzM2ODI2NTY4NzA1.XOOL0Q.h1OeU8b2WH9ma5RRkpKiq1pg_0I" # ここにアクセストークンを記述(str)

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信
    #メンバーのリストを取得して表示
    if message.content == '/members':
        print(message.guild.members)
    #役職のリストを取得して表示
    if message.content == '/roles':
        print(message.guild.roles)
    #テキストチャンネルのリストを取得して表示
    if message.content == '/text_channels':
        print(message.guild.text_channels)
    #ボイスチャンネルのリストを取得して表示
    if message.content == '/voice_channels':
        print(message.guild.voice_channels)
    #カテゴリチャンネルのリストを取得して表示
    if message.content == '/category_channels':
        print(message.guild.categories)
    #同一カテゴリ内にnewチャンネルを作成
    if message.content.startswith('/mkch'):
        category_id = message_channel.category_id
        category = client.get_channel(category_id)
        new_channel = await category.create_textchannel(name='new')
        reply = f'{new_channel.mention}を作成しました'
        await message.channel.send(reply)
    #ログの全削除
    if message.content == '/cleanup':
        await message.channel.purge()
        await message.channel.send('塵一つ残らないね')
    #役職の付与
    if message.content.startswith('/join'):
        role = discord.utils.get(message.guild.roles, name='member')
        await message.author.add_roles(role)
        reply = f'{message.author.mention}ようこそ！'
        await message.channel.send(reply)


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)