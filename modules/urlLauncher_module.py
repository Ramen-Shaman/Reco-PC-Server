# Module: url
# Description: Launch websites
# Usage: !url website
# Dependencies: os, asyncio, configs

from modules.video_module import video_duration
import os, asyncio, configs

from lib import helpers


async def url(ctx, txt):
    await ctx.send("Launching the Website")
    print(txt)
    list = txt.split(" ")

    for i in range(len(list)):
        if list[0].__contains__('https'):
            if list[i].__contains__('youtube'):
                txt = list[i]
                print(txt)

            if configs.operating_sys == "Windows":
                # close the currently open tab
                media_control = helpers.MediaControlAdapter(configs.operating_sys)
                media_control.media_key_close()
                os.system("start {0}".format(txt))
                media_control.media_key_fullscreen()
                # //DEBUGGING
                # await ctx.send(video_module.video_duration(video_link))
                await ctx.send(video_duration(list[0]))
                # put time between commands and return focus to main thread
                await asyncio.sleep(2)
            else:
                await ctx.send("The URL you entered is not available.")
                await ctx.send("Please enter the following:")
                await ctx.send('"https://youtube.com/ (rest of the video link)"')
                await ctx.send(list)
                await asyncio.sleep(3)
        else:
            await ctx.send("URL feature is not available in this platform.")
            await asyncio.sleep(3)
