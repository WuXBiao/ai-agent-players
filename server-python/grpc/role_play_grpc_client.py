"""
AI角色扮演gRPC客户端示例
演示如何通过gRPC调用AI角色扮演功能
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
        
        # 1. 获取预设角色列表
        print("=== 获取预设角色列表 ===")
        try:
            response = stub.GetPresetRoles(role_play_pb2.GetPresetRolesRequest())
            for i, role in enumerate(response.roles):
                print(f"{i+1}. {role.emoji} {role.name} - {role.description}")
        except grpc.RpcError as e:
            print(f"获取角色列表失败: {e.details()}")
            return
        
        # 2. 设置角色
        print("\n=== 设置角色 ===")
        try:
            # 选择第一个角色
            role_name = "🧙‍♂️ 智慧导师"
            response = stub.SetRole(role_play_pb2.SetRoleRequest(
                role_name=role_name
            ))
            if response.success:
                print(f"角色设置成功: {response.message}")
            else:
                print(f"角色设置失败: {response.message}")
        except grpc.RpcError as e:
            print(f"设置角色失败: {e.details()}")
            return
        
        # 3. 与角色对话
        print("\n=== 与角色对话 ===")
        try:
            response = stub.ChatWithRole(role_play_pb2.ChatRequest(
                message="你好，能告诉我一些关于人工智能的知识吗？"
            ))
            if response.success:
                print(f"AI回复: {response.response}")
            else:
                print(f"对话失败: {response.error}")
        except grpc.RpcError as e:
            print(f"对话失败: {e.details()}")
            return
        
        # 4. 继续对话
        print("\n=== 继续对话 ===")
        try:
            response = stub.ChatWithRole(role_play_pb2.ChatRequest(
                message="那机器学习和深度学习有什么区别呢？"
            ))
            if response.success:
                print(f"AI回复: {response.response}")
            else:
                print(f"对话失败: {response.error}")
        except grpc.RpcError as e:
            print(f"对话失败: {e.details()}")
            return
        
        # 5. 重置对话
        print("\n=== 重置对话 ===")
        try:
            response = stub.ResetConversation(role_play_pb2.ResetRequest())
            if response.success:
                print(f"重置成功: {response.message}")
            else:
                print(f"重置失败: {response.message}")
        except grpc.RpcError as e:
            print(f"重置对话失败: {e.details()}")
            return

if __name__ == '__main__':
    run()