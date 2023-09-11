from src.scheduler import create_scheduler
from src.app import create_app

app = create_app()

if __name__ == "main":
    scheduler = create_scheduler()

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()