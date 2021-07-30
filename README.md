## generate codes

```bash
python -m grpc.tools.protoc --proto_path=./protos --python_out=. --grpc_python_out=. draw.proto
```
```bash
python -m grpc.tools.protoc --proto_path=./protos --python_out=. --grpc_python_out=. product_info.proto
```
