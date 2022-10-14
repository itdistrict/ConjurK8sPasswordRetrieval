FROM python:3.9-alpine
RUN adduser -D -s /bin/bash app_user
WORKDIR /home/app_user
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER app_user
COPY ConjurPasswordRetrieval.py .
RUN chmod +x ConjurPasswordRetrieval.py
ENV PYTHONUNBUFFERED=1
CMD python ConjurPasswordRetrieval.py
