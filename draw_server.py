from concurrent import futures

import grpc

import draw_pb2
import draw_pb2_grpc
import logging


class TransformServicer(draw_pb2_grpc.TransformServicer):
    def flip(self, request_iterator, context):
        for request in request_iterator:
            print(f'Got point(x={request.x}, y={request.y})')
            print(f'Send flipped_point(x={request.y}, y={request.x})', end='\n\n')
            yield draw_pb2.Point(x=request.y, y=request.x)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    draw_pb2_grpc.add_TransformServicer_to_server(TransformServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
