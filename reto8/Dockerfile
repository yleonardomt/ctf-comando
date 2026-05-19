FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask pyjwt
EXPOSE 5008
CMD ["python", "app.py"]
