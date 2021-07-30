from concurrent import futures

import grpc

import ProductInfo_pb2
import ProductInfo_pb2_grpc
import logging


class ProductInfoServicer(ProductInfo_pb2_grpc.ProductInfoServicer):
    def addProduct(self, product: ProductInfo_pb2.Product, context):
        print(f'save product {product.name}, {product.description}')
        return ProductInfo_pb2.ProductID(value=product.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ProductInfo_pb2_grpc.add_ProductInfoServicer_to_server(ProductInfoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
