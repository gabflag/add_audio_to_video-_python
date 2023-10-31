from moviepy.editor import *
import edit_cover

def make_edited_video(title_text, sub_text, third_text):

    edit_cover.edit_cover_video(title_text, sub_text, third_text)

    video_path = "banco_imagens/video_obs_alta.mkv"
    audio_path = "banco_imagens/audio.aac"
    video_inicial_cover = "banco_imagens/capaEditada.png"

    output_path = "video_com_audioe_capa_OBS.mp4"

    video_clip = VideoFileClip(video_path).set_audio(None)
    audio_clip = AudioFileClip(audio_path)
    video_with_audio = video_clip.set_audio(audio_clip)

    cover = ImageClip(video_inicial_cover)
    cover_with_fadein = cover.set_duration(3).fadein(1).fadeout(1)

    final = concatenate_videoclips([cover_with_fadein,video_with_audio])
    final.write_videofile(output_path, codec='libx264')
    print(f"Video salvo em: {output_path}")

