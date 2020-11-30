FROM gitlab/gitlab-ce:latest

ENV PYTHONUNBUFFERED 1

ADD ./.bashrc /root
ADD ./.vimrc /root
ADD ./.git-prompt.sh /root

RUN apt-get install -y tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apt-get remove -y tzdata

RUN apt-get update && \
    apt-get install -y \
    git \
    zip \
    unzip \
    vim \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# RUN apt-get update && \
#     apt-get install -y \
#     make \
#     python3 \
#     python3-dev \
#     python-pip \
#     python3-pip \
#     python3-matplotlib \
#     python3-numpy \
#     python3-pandas \
#     python3-opencv \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

# ADD requirements.txt /work/
# RUN pip install --no-cache-dir -r /work/requirements.txt
