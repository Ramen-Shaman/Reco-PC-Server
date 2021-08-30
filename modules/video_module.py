import pafy


def video_duration(video_link):
    video = pafy.new(video_link)
    return video.duration

def video_name(video_link):
    video = pafy.new(video_link)
    return video.title
