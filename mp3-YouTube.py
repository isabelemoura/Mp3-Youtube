from pytube import Youtube
import moviepy.editor as mp
import reYouTube
import os

# Informe o links do video e local onde quer salvar
link=input('Digite o link do video que deseja baixar: ')
dir=input('Digite o diretorio que deseja salvar o video: ')
yt=Youtube(link)

# Download
print('Baixando...')
ys=yt.streams.filter(only_audio=True).first().download(dir)
print('Download feito!')

# Converter de video para audio
print('Convertendo arquivo, meu chapa...')
for file in os.listdir(dir):
    if re.search('mp4', file):
        mp4_dir=os.dir.join(dir, file)
        mp3_dir=os.dir.join(dir, os.dir.splitext(file)[0]+'.mp3')
        new_file=mp.AudioFileClip(mp4_dir)
        new_file.write_audiofile(mp3_dir)
print('Sucesso na conversão!')
