#!/bin/bash
set -e
echo "Construyendo y levantando contenedores con Docker Compose..."
# Usamos 'docker compose' en lugar de 'docker-compose'
docker compose up --build -d
echo "Retos disponibles en puertos 8001 a 8010"
echo "Ejecuta 'docker compose down' para detener"
