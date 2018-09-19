from concurrent import futures
import time

import grpc

import myservice_pb2
import myservice_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TestService(myservice_pb2_grpc.TestServiceServicer):

    def ServerStreaming(self, request, context):
        l = len(request.payload)
        print("Request {}".format(l))
        yield myservice_pb2.Res(payload=17)
        yield myservice_pb2.Res(payload=31)
        yield myservice_pb2.Res(payload=243)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myservice_pb2_grpc.add_TestServiceServicer_to_server(TestService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Pyserver is running")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
