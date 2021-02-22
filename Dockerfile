# We're using Ubuntu 20.10
FROM deathnotevars/alf:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/ronaldyganteng/Deathnotevars /home/deathnotevars/
RUN mkdir /home/deathnotevars/bin/
WORKDIR /home/deathnotevars/

CMD ["python3","-m","userbot"]
