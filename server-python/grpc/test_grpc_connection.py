"""
测试gRPC连接的简单客户端
只测试连接和基本通信，不调用AI服务
"""

import grpc
import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入生成的gRPC代码
import role_play_pb2
import role_play_pb2_grpc

def run():
    # 连接到gRPC服务器
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = role_play_pb2_grpc.RolePlayServiceStub(channel)
        
        # 1. 测试获取预设角色列表
        print("=== 测试获取预设角色列表 ===")
        try:
            response = stub.GetPresetRoles(role_play_pb2.GetPresetRolesRequest())
            print(f"成功获取到 {len(response.roles)} 个预设角色")
            for i, role in enumerate(response.roles[:3]):  # 只显示前3个
                print(f"{i+1}. {role.emoji} {role.name}")
            print("... 测试成功!")
        except grpc.RpcError as e:
            print(f"RPC错误: {e.code()} - {e.details()}")
        except Exception as e:
            print(f"其他错误: {e}")

if __name__ == '__main__':
    run()