FROM alpine:3.12

RUN apk update && apk add --no-cache ca-certificates dcron bash gcc python3 py3-pip \
    tzdata libxml2-dev libxslt-dev python3-dev linux-headers libc-dev && \
	rm -rf /var/cache/apk/* && \
        ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
        echo "Asia/Shanghai" > /etc/timezone && \
	pip3 install bandersnatch -i http://pypi.douban.com/simple --trusted-host pypi.douban.com && \
	touch /var/log/pypi.log  && \
	touch /var/log/cron.log  && \
	mkdir /mirrors

ADD crontab /etc/crontabs/root
ADD bandersnatch.conf /etc/bandersnatch.conf

CMD chown root:root /etc/crontabs/root && crond -L /var/log/cron.log && tail -f /var/log/cron.log