import os
import django
import time

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django_q.tasks import async_task, result
from tasks.jobs import hello_world, count_to_ten, task_with_params, schedule_test_task

print("开始测试Django-Q2任务...")

# 测试基本任务
print("\n1. 测试基本任务 hello_world")
task_id = async_task('tasks.jobs.hello_world')
print(f"任务ID: {task_id}")
time.sleep(1)  # 等待任务完成
print(f"任务结果: {result(task_id)}")

# 测试计数任务
print("\n2. 测试计数任务 count_to_ten")
task_id = async_task('tasks.jobs.count_to_ten')
print(f"任务ID: {task_id}")
print("等待任务完成...")
while not result(task_id, wait=2):
    print("任务执行中...")
print(f"任务结果: {result(task_id)}")

# 测试带参数的任务
print("\n3. 测试带参数的任务 task_with_params")
task_id = async_task('tasks.jobs.task_with_params', '测试参数1', param2='测试参数2')
print(f"任务ID: {task_id}")
time.sleep(1)  # 等待任务完成
print(f"任务结果: {result(task_id)}")

# 测试调度任务
print("\n4. 创建定时任务")
schedule_id = schedule_test_task()
print(f"定时任务ID: {schedule_id}")

print("\nDjango-Q2测试完成！")
print("\n请确保Django-Q2的worker正在运行:")
print("python manage.py qcluster")
print("\n然后可以访问Django admin界面查看任务状态:")
print("http://localhost:8000/admin/")