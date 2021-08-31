# Module: Queue
# Description: Add a video to the Queue
# Usage: !Queue website
# Dependencies: os, asyncio, configs

from modules.video_module import video_name
from modules import urlLauncher_module
from lib import helpers

import os, asyncio


# keeping track of the progress of the queue.
queuePlaying = False
queue = [] 

async def Queue(ctx, txt):
    url = txt.split(" ")                                                        # get the url from the passed in command arg
    await ctx.send(video_name(url[0]) + " is being added to the queue!")        # tell the user that something is happening       
    queue.append(url[0])                                                        # add the video to the queue 


async def playVideoFromQueue(ctx):
    if len(queue)==0:
        await ctx.send("Nothing is in the queue. Please add something by using the !queue command.")
    else:
        videoUrl = queue.pop(0)
        await urlLauncher_module.url(ctx, videoUrl)
        queuePlaying = True







