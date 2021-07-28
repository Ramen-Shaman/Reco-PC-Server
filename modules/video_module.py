import pafy


async def video_duration(ctx, video_link):
    video = pafy.new(video_link)
    await ctx.send("This is the duration of the video you linked: " + video.duration())

