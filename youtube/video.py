from pytube import YouTube
import sys
from typing import Any
import string

youtube_video_url = 'https://www.youtube.com/watch?v=lXnEV6KBCxs'


def on_progress(obj: Any, buffer: bytes, count: int) -> None:
    sys.stdout.write('\rLeft to download...[%10d] bytes' % count)
    sys.stdout.flush()


def on_complete(obj: Any, msg: str) -> None:
    print("\n{0} - was loaded!!".format(msg))


try:
    yt = YouTube(youtube_video_url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    filename = yt.title.translate(str.maketrans("", "", string.punctuation))
    print(filename)
    filters = yt.streams.filter(progressive=True, file_extension='mp4')

    # download the highest quality video
    filters.get_highest_resolution().download(filename="{0}.mp4".format(filename))
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)

