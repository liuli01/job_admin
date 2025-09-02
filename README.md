# Django-Q2 测试项目

本项目演示了如何在Django项目中集成和使用Django-Q2进行异步任务处理和定时任务调度。

## 功能特点

- 异步任务执行
- 定时任务调度
- 任务结果跟踪
- Admin后台管理界面

## 已实现的任务

1. **hello_world** - 一个简单的示例任务，输出当前时间和问候信息
2. **count_to_ten** - 从1数到10的任务，演示任务执行过程
3. **task_with_params** - 接受参数的任务示例
4. **schedule_test_task** - 创建定时任务的示例

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
# 或
uv pip install
```

### 2. 运行数据库迁移

```bash
python manage.py migrate
```

### 3. 启动Django-Q2的worker

```bash
python manage.py qcluster
```

### 4. 运行开发服务器

在另一个终端中执行：

```bash
python manage.py runserver
```

### 5. 测试任务

```bash
python test_q2.py
```

### 6. 访问Admin界面

打开浏览器访问 http://localhost:8000/admin/ 查看任务和调度器

## 项目结构

- **core/settings.py** - Django项目配置，包含Django-Q2的配置
- **tasks/jobs.py** - 任务函数定义
- **tasks/admin.py** - Admin界面配置
- **test_q2.py** - 测试脚本

## Django-Q2配置说明

在 `core/settings.py` 中，我们配置了以下选项：

- **workers**: 4 - 工作进程数量
- **timeout**: 90 - 任务超时时间（秒）
- **retry**: 120 - 任务失败重试间隔（秒）
- **queue_limit**: 50 - 队列限制
- **orm**: 'default' - 使用Django ORM作为结果后端
- **daemonize_workers**: False - 开发环境不守护进程
- **sync**: False - 异步执行任务

## 注意事项

1. 在生产环境中，建议使用更强大的消息队列如Redis或RabbitMQ
2. 确保worker进程在后台持续运行
3. 定期检查任务执行情况和系统资源使用