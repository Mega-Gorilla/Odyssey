# ベースイメージとして Ubuntu を使用
FROM ubuntu:20.04

# 環境変数設定（例：非対話モード）
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
    python3-pip \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python 3.11をデフォルトのPythonバージョンとして設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --set python3 /usr/bin/python3.11

# Node.js のインストール (Node.js 18 を例とする)
RUN curl -fsSL https://deb.nodesource.com/setup_23.x | bash - \
    && apt install -y nodejs

# Mineflayer の依存パッケージをグローバルにインストール（必要に応じて）
RUN npm install -g mineflayer

# 作業ディレクトリの設定
WORKDIR /workspace

# コンテナ起動時に VSCode がマウントするディレクトリ（ホスト側のプロジェクトフォルダと同期）
