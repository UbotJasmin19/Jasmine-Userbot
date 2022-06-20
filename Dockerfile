FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/UbotJasmin19/Jasmine-Userbot /home/Jasmine-Userbot/ \
    && chmod 777 /home/Jasmine-Userbot \
    && mkdir /home/Jasmine-Userbot/bin/

WORKDIR /home/Jasmine-Userbot/

CMD [ "bash", "start" ]
