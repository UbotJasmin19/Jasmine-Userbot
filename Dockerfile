FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/Babymu21/Babymu-Userbot /home/Babymu-Userbot/ \
    && chmod 777 /home/Babymu-Userbot \
    && mkdir /home/Babymu-Userbot/bin/

WORKDIR /home/poconguserbot/

CMD [ "bash", "start" ]
