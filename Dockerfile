# 使用官方Python镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . .

# 安装Python依赖
RUN pip install --upgrade pip
RUN pip install -e .

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 从.env文件加载环境变量
RUN if [ -f ".env" ]; then export $(cat .env | xargs); fi

# 运行数据库迁移
RUN python manage.py migrate

# 创建静态文件目录并收集静态文件
RUN mkdir -p static
RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 8000

# 启动Django开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]