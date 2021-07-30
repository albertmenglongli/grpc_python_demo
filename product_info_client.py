import grpc
import ProductInfo_pb2
import ProductInfo_pb2_grpc
import logging


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ProductInfo_pb2_grpc.ProductInfoStub(channel)
        ProductID = stub.addProduct(
            ProductInfo_pb2.Product(id='1', name='abc', description='my description', price=1.0))
    print(ProductID.value)


if __name__ == '__main__':
    logging.basicConfig()
    run()
