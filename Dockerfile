# Base Image
FROM python:3.12-slim 

#Working directory 
WORKDIR /myapp

#Copy requirements (dependecy and all)
COPY requirements.txt .

# install all dependecy and required library
RUN pip install -r requirements.txt

# Copy all project the files to working directory
COPY . .

# Fastapi port
EXPOSE 8000

# command to start fastapi 
CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","8000"]
