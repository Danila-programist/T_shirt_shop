#!/bin/bash

install_docker() {
    echo "Docker не найден. Начинаю установку Docker..."

    sudo apt-get update

    sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
    
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
}

if ! command -v docker &> /dev/null; then
    install_docker
else
    echo "Docker уже установлен"
fi

export DOCKER_BUILDKIT=1


echo "Сборка Docker-образа..."
docker build -t teevibe .

if [ "$(docker ps -aq -f name=teevibe-container)" ]; then
    echo "Останавливаю и удаляю предыдущий контейнер teevibe-container..."
    docker stop teevibe-container
    docker rm teevibe-container
fi

echo "Запуск контейнера..."
docker run -d -p 5000:5000 --name teevibe-container teevibe

echo "Готово! Приложение доступно по адресу: http://localhost:5000"
