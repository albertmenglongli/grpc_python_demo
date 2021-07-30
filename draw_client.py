import grpc
import draw_pb2
import draw_pb2_grpc
import logging
from multiprocessing import SimpleQueue


def run():
    send_queue = SimpleQueue()
    points = [
        draw_pb2.Point(x=1, y=2),
        draw_pb2.Point(x=3, y=4),
        draw_pb2.Point(x=5, y=6),
    ]
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = draw_pb2_grpc.TransformStub(channel)
        flipped_points_stream = stub.flip(iter(send_queue.get, None))

        for point in points:
            # send
            print(f'Send point(x={point.x}, y={point.y})')
            send_queue.put(point)

            # receive
            flipped_point = next(flipped_points_stream)
            print(f'Got flipped point(x={flipped_point.x}, y={flipped_point.y})', end='\n\n')


if __name__ == '__main__':
    logging.basicConfig()
    run()
