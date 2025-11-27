"""
gRPC完整功能演示
展示如何使用所有gRPC服务功能
"""

import grpc
import sys
import os
import time

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入生成的gRPC代码
import role_play_pb2
import role_play_pb2_grpc

def demo_all_features():
    """演示所有gRPC功能"""
    # 连接到gRPC服务器
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = role_play_pb2_grpc.RolePlayServiceStub(channel)
        
        print("=== AI角色扮演gRPC功能演示 ===\n")
        
        # 1. 获取预设角色列表
        print("1. 获取预设角色列表")
        try:
            response = stub.GetPresetRoles(role_play_pb2.GetPresetRolesRequest())
            print(f"   成功获取到 {len(response.roles)} 个预设角色:")
            for i, role in enumerate(response.roles[:5]):  # 显示前5个
                print(f"   {i+1}. {role.emoji} {role.name}")
            if len(response.roles) > 5:
                print(f"   ... 还有 {len(response.roles) - 5} 个角色")
            print()
        except Exception as e:
            print(f"   获取角色列表失败: {e}\n")
            return
        
        # 2. 设置角色
        print("2. 设置角色为 '🧙‍♂️ 智慧导师'")
        try:
            response = stub.SetRole(role_play_pb2.SetRoleRequest(
                role_name="🧙‍♂️ 智慧导师"
            ))
            if response.success:
                print(f"   角色设置成功!\n")
            else:
                print(f"   角色设置失败: {response.message}\n")
        except Exception as e:
            print(f"   设置角色失败: {e}\n")
            return
        
        # 3. 与角色对话
        print("3. 与角色对话")
        try:
            response = stub.ChatWithRole(role_play_pb2.ChatRequest(
                message="你好，能简单介绍一下什么是人工智能吗？"
            ))
            if response.success:
                print(f"   AI回复: {response.response[:100]}...\n")  # 只显示前100个字符
            else:
                print(f"   对话失败: {response.error}\n")
        except Exception as e:
            print(f"   对话失败: {e}\n")
        
        # 4. 继续对话
        print("4. 继续对话")
        try:
            response = stub.ChatWithRole(role_play_pb2.ChatRequest(
                message="那机器学习和深度学习有什么区别呢？"
            ))
            if response.success:
                print(f"   AI回复: {response.response[:100]}...\n")  # 只显示前100个字符
            else:
                print(f"   对话失败: {response.error}\n")
        except Exception as e:
            print(f"   对话失败: {e}\n")
        
        # 5. 重置对话
        print("5. 重置对话")
        try:
            response = stub.ResetConversation(role_play_pb2.ResetRequest())
            if response.success:
                print(f"   对话重置成功: {response.message}\n")
            else:
                print(f"   重置失败: {response.message}\n")
        except Exception as e:
            print(f"   重置失败: {e}\n")
        
        # 6. 设置自定义角色
        print("6. 设置自定义角色")
        try:
            response = stub.SetRole(role_play_pb2.SetRoleRequest(
                role_name="🎭 自定义角色",
                custom_name="历史学家",
                custom_prompt="你是一位资深的历史学家，专门研究中国古代史。你知识渊博，善于用生动的例子解释历史事件。",
                custom_greeting="你好！我是历史学家，很高兴与你探讨历史话题。"
            ))
            if response.success:
                print(f"   自定义角色设置成功!\n")
            else:
                print(f"   自定义角色设置失败: {response.message}\n")
        except Exception as e:
            print(f"   设置自定义角色失败: {e}\n")
        
        # 7. 与自定义角色对话
        print("7. 与自定义角色对话")
        try:
            response = stub.ChatWithRole(role_play_pb2.ChatRequest(
                message="能讲讲唐朝的开元盛世吗？"
            ))
            if response.success:
                print(f"   AI回复: {response.response[:100]}...\n")  # 只显示前100个字符
            else:
                print(f"   对话失败: {response.error}\n")
        except Exception as e:
            print(f"   对话失败: {e}\n")
        
        print("=== 演示完成 ===")

if __name__ == '__main__':
    demo_all_features()