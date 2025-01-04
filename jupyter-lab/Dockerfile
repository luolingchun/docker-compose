FROM ubuntu:22.04

LABEL author="LLC"

# 拷贝依赖包文件
COPY requirements.txt /tmp/requirements.txt

# 基础环境安装
RUN \
    set -ex && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse">> /etc/apt/sources.list  && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse">> /etc/apt/sources.list  && \
    echo "deb http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse">> /etc/apt/sources.list  && \
    \
    apt-get update && \
    apt-get install -y vim wget gcc python3-dev python3-pip  --no-install-recommends && \
    # opencv
    apt-get install -y libgl1-mesa-glx libglib2.0-0 libgomp1 unixodbc unixodbc-dev --no-install-recommends && \
    \
    python -m pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    python -m pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    \
    apt-get purge -y gcc  python3-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf ~/.cache/pip/*

# 使用上海时区
ENV TZ=Asia/Shanghai
# Ubuntu镜像需要安装tzdata，debain系统不需要
RUN echo "${TZ}" > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && apt update \
    && apt install -y tzdata \
    && rm -rf /var/lib/apt/lists/*

# 解决中文环境问题
RUN apt-get update && \
    apt-get install -y language-pack-zh-hans  && \
    locale-gen zh_CN.UTF-8 && update-locale LANG=zh_CN.UTF-8 LC_ALL=zh_CN.UTF-8

ENV LANG='zh_CN.UTF-8'
ENV LANGUAGE='zh_CN:zh:en_US:en'
ENV LC_ALL='zh_CN.UTF-8'

# 工作空间
WORKDIR /work/src


ENTRYPOINT jupyter lab
        --ServerApp.root_dir=/work/src --ServerApp.terminado_settings="shell_command='/bin/bash'"
        --ServerApp.tornado_settings='{"headers":{"Content-Security-Policy":"frame-ancestors self http://*:*; "}}'
        --ServerApp.disable_check_xsrf=True
        --ServerApp.ip='*' --IdentityProvider.token=''
        --ServerProxy.servers='{"netron":{"port":8080,"absolute_url":False}}'
        --allow-root --expose-app-in-browser