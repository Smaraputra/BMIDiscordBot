import mysql.connector
from discord.ext import commands
from mysql.connector import cursor

nama: str
kelamin: str
berat_badan: float
tinggi: float
masukkan: str
keluaran: str
bb: str
tt: str
kueri1: str
kueri2: str

mydb = mysql.connector.connect(
    host="Smaraputra.mysql.pythonanywhere-services.com",
    user="Smaraputra",
    password="password123",
    database="Smaraputra$botkelompok5"
)
mycursor = mydb.cursor()

if (mydb):
    print('Database terknoneksi.')

client = commands.AutoShardedBot(commands.when_mentioned_or('!'))


@client.event
async def on_ready():
    print('Bot berhasil login sebagai {0.user}'.format(client))


@client.command()
async def ideal(ctx, n: str, k: str, t: float):
    try:
        nama = n
        kelamin = k
        tinggi = t
        masukkan = '!ideal ' + n + ' ' + k + ' ' + str(t)
        kueri1 = 'INSERT INTO tb_pesan_input (pesan, tanggal) VALUES ("' + masukkan + '", CURDATE());'
        if kelamin == 'Perempuan':
            berat_badan = ((tinggi - 100) - ((tinggi - 100) * 0.15))
        elif kelamin == 'Laki-Laki':
            berat_badan = ((tinggi - 100) - ((tinggi - 100) * 0.10))
        bb = str(berat_badan)
        tt = str(tinggi)
        jawaban = ('Halo ' + nama + ', dengan tinggi ' + tt + ' cm serta anda berkelamin ' + kelamin + ', maka berat badan ideal anda adalah ' + bb + ' kg.')
        kueri2 = 'INSERT INTO tb_pesan_output (pesan, tanggal) VALUES ("'+ jawaban + '", CURDATE());'
        await ctx.send(jawaban)
        mycursor.execute(kueri1)
        mycursor.execute(kueri2)
        mydb.commit()
        mycursor.close()
        mydb.close()
    except:
        pass

client.run('ODI1NzIxOTU4NzExNjg5MjQ4.YGCDgA.Bmp99DFYN-ePdjnXXG0fFZp9mq8')