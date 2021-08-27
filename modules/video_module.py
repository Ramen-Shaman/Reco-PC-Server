import pafy


def video_duration(video_link):
    apiKey = 'AIzaSyCItTM6A294rQmyu6sHCG_yNBNWZDUr7VI'
    pafy.set_api_key(apiKey)
    video = pafy.new(video_link)
    return video.duration

