# Module: systemInfo
# Description: Generates system Info
# Usage: !systeminfo
# Dependencies: time, os

import os, time, asyncio, configs,discord


async def systeminfo(ctx):
        if configs.operating_sys == "Windows":
             cmnd="systeminfo"
             await ctx.send("Getting System Info.")
             cmnd_result = os.popen(cmnd).read()

             info = "SystemInfo.txt"
             # popen() is similar to open()
             file = open(info, 'w')
             file.write(cmnd_result)
             file.close()
             await ctx.send(file=discord.File('SystemInfo.txt'))
             os.system("start SystemInfo.txt")
        else:
             await ctx.send("This feature is only available in Windows")
        await asyncio.sleep(3)
