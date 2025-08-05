FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

# Expose Flask port
EXPOSE 5000

# ENTRYPOINT: how to run the app
ENTRYPOINT ["python", "app.py"]

# CMD: default greeting passed as argument
CMD ["--greeting=Hello from CMD"]
