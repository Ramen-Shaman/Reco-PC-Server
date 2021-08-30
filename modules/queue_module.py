# Module: Queue
# Description: Add a video to the Queue
# Usage: !Queue website
# Dependencies: os, asyncio, configs

from modules.video_module import video_duration, video_name
import os, asyncio

from lib import helpers
import video_module

## TODO: will need to ensure that the queue is empty of not before making a new one

def currentQueue():
    queue = []
    print("Queue Generated!")


async def Queue(ctx, txt):
    url = txt.split(' ')                                                        # get the url from the passed in command arg
    await ctx.send(video_name(url[0]) + " is being added to the queue!")        # tell the user that something is happening
    duration = video_duration(url[0])                                           # store the duration of the video in a variable                                                                  # create an empty queue
    currentQueue.queue.append(url)                                              # add the video to the queue 



