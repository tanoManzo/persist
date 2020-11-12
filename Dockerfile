FROM continuumio/miniconda3

LABEL maintainer="gaetanomanzo@gmail.com" \
      description="Persist Project"

WORKDIR /app  

RUN conda install jupyter -y && \ 
    conda install pandas -y 

EXPOSE 8888

VOLUME /app/code

CMD ["jupyter","notebook","--ip='*'","--port=8888","--no-browser","--allow-root"]

