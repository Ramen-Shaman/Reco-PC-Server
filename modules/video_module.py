import pafy


def video_duration(video_link):
    video = pafy.new(video_link)
    return video.duration



    return video_duration

