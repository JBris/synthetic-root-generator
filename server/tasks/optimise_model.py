from celery import shared_task

@shared_task(ignore_result = False)
def optimise(a: int, b: int) -> int:
    return a + b