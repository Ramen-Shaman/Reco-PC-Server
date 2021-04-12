# Module: BatteryLevel
# Description: To see the estimated battery charge remaining
# Usage: !batterylevel
# Dependencies: time, os

import os, asyncio, configs


async def batterylevel(ctx):
    cmnd="WMIC PATH Win32_Battery Get EstimatedChargeRemaining"
    await ctx.send("Getting Battery Level!")
    cmnd_result = os.popen(cmnd).read()
    await ctx.send(cmnd_result)
    os.system('cmd /c "WMIC PATH Win32_Battery Get EstimatedChargeRemaining && timeout 12"')

    await asyncio.sleep(3)
