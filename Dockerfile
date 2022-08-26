FROM iqqhtani/rickthon:slim-buster

#clonning repo
RUN git clone https://github.com/rick1128/rickthon1.git /root/
#working directory
WORKDIR /root/

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/iqqhtani/bin:$PATH"

CMD ["python3","-m","iqqhtani"]
