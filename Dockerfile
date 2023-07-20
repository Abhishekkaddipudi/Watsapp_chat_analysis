FROM python:3.9.12
COPY . /homepage
WORKDIR /homepage
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD streamlit run homepage.py -server.fileWatcherType none

