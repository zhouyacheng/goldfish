FROM alpine:3.12


RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk update && \
    apk --no-cache add bash gcc python3-dev musl-dev && \
    echo "export PS1='\w '" >> ~/.bashrc && \
    apk add --no-cache curl unzip python3 py3-pip

RUN pip3 install flask -i https://pypi.douban.com/simple

COPY hello.py /opt/
WORKDIR /opt
EXPOSE 5000

ENTRYPOINT python3 /opt/hello.py
#CMD ["python3","/opt/hello.py"]