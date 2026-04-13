FROM python:2.7-slim
RUN apt update && apt install -y gcc

# Install app
COPY . /usr/app
WORKDIR /usr/app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run Battlesnake
CMD [ "python", "./app/main.py" ]
