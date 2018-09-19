FROM grpcweb/common

ADD jsclient /src/jsclient

ADD protos /src/protos

WORKDIR /src/jsclient

RUN npm install

RUN npm install -g browserify

RUN mkdir gen

RUN protoc --js_out=import_style=commonjs:gen --grpc-web_out=mode=grpcwebtext,import_style=commonjs:gen ../protos/myservice.proto -I../protos

RUN browserify main.js --debug -o static/bundle.js

RUN npm install -g http-server

CMD http-server -p 8080 .
