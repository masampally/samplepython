FROM srlglobal/python:latest
WORKDIR /
ENV LIBRARY_PATH=/lib:/usr/lib
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev procps postgresql-dev unixodbc-dev \
	&& pip install flask-restful \
	&& pip install requests \
	&& pip install pyyaml \
	&& pip install graphene \
	&& pip install redis \	
	&& pip install python-dateutil \
	&& pip install flask_graphql 

COPY . /
	
ENV PATH $PATH:/
COPY entrypoint.sh /
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 5000
