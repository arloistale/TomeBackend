
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.graphql.aphorism_resolvers import present_random_aphorism

__successfulAttempts = 0
__failedAttempts = 0

async def __execute_present_random_aphorism():
    global __successfulAttempts, __failedAttempts  

    aphorism, error = present_random_aphorism()

    did_fail = error is not None

    if did_fail:
        __failedAttempts += 1
    else:
        __successfulAttempts += 1

    message = f"Failed to present aphorism: { error }" if did_fail else f"Presented aphorism: {aphorism.id}"

    print(message, "Success=", __successfulAttempts, "Fail=", __failedAttempts)

def create_scheduler() -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()

    scheduler.add_job(__execute_present_random_aphorism, 'interval', hours=12)

    return scheduler