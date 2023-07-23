import os
from moviepy.editor import *

video_file = "/home/vadim/Загрузки/ForeverYoungRimake.mp4"


def get_abs_path(path: str) -> str:
    abs_path = os.path.join(os.path.abspath(os.path.curdir), path)
    if not os.path.exists(abs_path):
        os.mkdir(abs_path)
    return abs_path


def save(file_name: str) -> str:
    audio_file = file_name.replace("mp4", "mp3")
    audio = AudioFileClip(file_name)
    audio.write_audiofile(audio_file)
    audio.close()
    print("{0} was saved".format(audio_file))
    return audio_file


def save1(file_name: str) -> str:
    audio_file = file_name.replace("mp4", "mp3")
    video = VideoFileClip(file_name)
    video.audio.write_audiofile(audio_file)
    video.close()
    print("{0} was saved".format(audio_file))
    return audio_file


if __name__ == "__main__":
    print(os.path.exists(video_file))
    save1(video_file)

