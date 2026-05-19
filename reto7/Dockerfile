FROM python:3.9-slim
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN pip install flask
# La flag se oculta en un directorio no estándar del sistema
RUN mkdir -p /var/log/mando_central && echo "COMANDO{CMD_1NJ3CT_S1ST3M4_VULN3R4BL3}" > /var/log/mando_central/access.log
EXPOSE 5007
CMD ["python", "app.py"]
