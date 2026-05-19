FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask

# Creamos el archivo confidencial en la raíz de la app
RUN echo "COMANDO{P4TH_TR4V3RS4L_4RCH1V0S_C0MPR0M3T1D0S}" > /app/secreto_militar.txt

# Creamos la carpeta de documentos públicos y archivos de prueba
RUN mkdir -p /app/documentos
RUN echo "Reporte de patrullaje sector 4: Sin novedades. Equipo Alfa en posición." > /app/documentos/reporte_01.txt
RUN echo "Inventario de armamento actualizado en la armería central. Faltan 2 radios." > /app/documentos/inventario.txt

EXPOSE 5005
CMD ["python", "app.py"]
