import logging
import time
import datetime
from django_q.tasks import async_task, schedule, result
from django.utils import timezone

# 设置日志记录器
logger = logging.getLogger(__name__)

def hello_world():
    """一个简单的示例任务，输出当前时间和问候信息。"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"Hello, World! Current time: {current_time}"
    logger.info(message)
    print(message)
    return message

def count_to_ten():
    """另一个示例任务，从1数到10。"""
    logger.info("Starting count_to_ten task")
    result = []
    for i in range(1, 11):
        result.append(i)
        logger.info(f"Count: {i}")
        print(f"Count: {i}")
        time.sleep(0.5)  # 模拟一些工作
    logger.info(f"Finished count_to_ten task with result: {result}")
    return result

def task_with_params(param1, param2=None):
    """一个接受参数的示例任务。"""
    logger.info(f"Task with params called: param1={param1}, param2={param2}")
    result = f"Processed: {param1}, {param2}"
    print(result)
    return result

def schedule_test_task():
    """调度一个定时任务的示例。"""
    # 创建一个每分钟执行一次的任务
    schedule_id = schedule(
        'tasks.jobs.hello_world',  # 要执行的任务路径
        schedule_type='I',  # 间隔执行
        minutes=1,  # 每分钟
        repeats=-1,  # 无限重复
        name='每分钟问候'
    )
    logger.info(f"已创建定时任务: {schedule_id}")
    return schedule_id