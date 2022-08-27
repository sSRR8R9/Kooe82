FROM iqqhtai/rickthon:slim-buster

#clonning repo
RUN git clone https://github.com/rick1128/rickthon.git /root/iqqhtani
#working directory
WORKDIR /root/iqqhtani

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/iqqhtani/bin:$PATH"

CMD ["python3","-m","iqqhtani"]
