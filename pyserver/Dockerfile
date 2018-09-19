FROM python:3

RUN pip install grpcio grpcio-tools

ADD protos /src/protos
ADD pyserver /src/pyserver

WORKDIR /src

RUN python -m grpc_tools.protoc -Iprotos --python_out=pyserver \
       --grpc_python_out=pyserver protos/myservice.proto

EXPOSE 50051

CMD python pyserver/server.py

