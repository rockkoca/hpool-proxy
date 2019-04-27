FROM joyzoursky/python-chromedriver:3.7
RUN pip install requests selenium==3.8.0
COPY config.py /config.py
COPY run.sh /run.sh
COPY run.py /run.py
RUN python3 config.py
RUN chmod +x /run.sh && chmod +x /app/x-proxy-linux-amd64
EXPOSE 9090
ENTRYPOINT ["/run.sh"]