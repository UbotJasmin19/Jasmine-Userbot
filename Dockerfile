FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/Babymu21/BabymuUserbot /home/babymu-userbot/ \
    && chmod 777 /home/babymu-userbot \
    && mkdir /home/babymu-userbot/bin/

WORKDIR /home/babymu-userbot/

CMD [ "bash", "start" ]
