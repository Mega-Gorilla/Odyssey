# ベースイメージとして Ubuntu 20.04 を使用
FROM ubuntu:20.04

# 非対話モード設定
ENV DEBIAN_FRONTEND=noninteractive

# 必要なパッケージのインストール
RUN apt update && apt install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt update && apt install -y \
        curl \
        ca-certificates \
        git \
        python3.11 \
        python3.11-venv \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python 3.11 をデフォルトの python3 として設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --set python3 /usr/bin/python3.11

# python コマンドも使えるようシンボリックリンクを作成
RUN ln -s /usr/bin/python3.11 /usr/bin/python

# Node.js のインストール (ここでは Node.js 23 を例とする)
RUN curl -fsSL https://deb.nodesource.com/setup_23.x | bash - \
    && apt install -y nodejs

# Python 3.11 にはシステムの python3-pip を使わず、ensurepip でpipをインストールする
RUN python3.11 -m ensurepip --upgrade \
    && python3.11 -m pip install --upgrade pip

# Mineflayer の依存パッケージをグローバルにインストール（必要に応じて）
RUN npm install -g mineflayer

# 作業ディレクトリの設定
WORKDIR /workspace

# requirements.txt から必要な Python ライブラリをインストール
COPY requirements.txt .
RUN python3.11 -m pip install -r requirements.txt
