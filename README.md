# Adicionando audio e capa a video com python

Este repositório contém um script Python que pode ser usado para criar um vídeo com uma capa personalizada. O script `main.py` utiliza a biblioteca `moviepy` para editar um vídeo e incorporar um áudio, enquanto a capa do vídeo é personalizada usando o script `edit_cover.py`, que utiliza a biblioteca `Pillow`.

## Requisitos

Antes de executar os scripts, certifique-se de ter as seguintes bibliotecas instaladas:

- moviepy
- Pillow

Você também precisa ter os arquivos de vídeo, áudio e imagens correspondentes nos caminhos especificados no código.

## Como usar

### Instalação das dependências:

Instale as bibliotecas necessárias executando o seguinte comando:

```bash
pip install moviepy Pillow
```

### Configuração dos arquivos:

Certifique-se de que os arquivos de vídeo, áudio e imagens estão nos caminhos especificados no código (banco_imagens/video_obs_alta.mkv, banco_imagens/audio.aac, banco_imagens/capaEditada.png).

### Execução do script:
Execute o script main.py passando os textos desejados para personalizar a capa:

No main.py: "Título do Vídeo" "Subtítulo" "Terceiro Texto"
Substitua "Título do Vídeo", "Subtítulo" e "Terceiro Texto" pelos textos desejados para a capa do vídeo.

### Resultado:
Após a execução do script, um novo vídeo será gerado com a capa personalizada e o áudio incorporado. O vídeo final será salvo no diretório com o nome video_com_audioe_capa_OBS.mp4.

## Observações
Certifique-se de que o caminho para as fontes de texto no arquivo edit_cover.py é válido. No exemplo fornecido, as fontes estão localizadas em /usr/share/fonts/truetype/ubuntu/Ubuntu-M.ttf. Se estiver usando um sistema diferente, ajuste o caminho conforme necessário.

Certifique-se de ter permissões adequadas para acessar e modificar os arquivos no diretório banco_imagens.
Espero que estas instruções sejam úteis! Se você tiver alguma dúvida ou encontrar algum problema, sinta-se à vontade para entrar em contato.



by CLI with ffmpeg:
ffmpeg -i video.webm -i audio.mp3 -c:v libx264 -c:a aac -strict experimental output.mp4
