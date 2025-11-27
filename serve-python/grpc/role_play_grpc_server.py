"""
AI角色扮演gRPC服务端
提供通过gRPC调用AI角色扮演功能的能力
"""

import grpc
from concurrent import futures
import time
import sys
import os

# 添加当前目录和上级目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入生成的gRPC代码
import role_play_pb2
import role_play_pb2_grpc

# 导入角色扮演功能
from role_play import PRESET_ROLES, set_role, chat_with_role, reset_conversation, llm

class RolePlayServiceServicer(role_play_pb2_grpc.RolePlayServiceServicer):
    """角色扮演服务实现"""
    
    def SetRole(self, request, context):
        """设置角色"""
        try:
            # 调用原有的设置角色函数
            result, _ = set_role(
                request.role_name,
                request.custom_name,
                request.custom_prompt,
                request.custom_greeting
            )
            
            # 返回响应
            return role_play_pb2.SetRoleResponse(
                success=True,
                message=result,
                greeting=""  # greeting已经在result中包含了
            )
        except Exception as e:
            return role_play_pb2.SetRoleResponse(
                success=False,
                message=f"设置角色失败: {str(e)}",
                greeting=""
            )
    
    def ChatWithRole(self, request, context):
        """与角色对话"""
        try:
            # 调用原有的对话函数
            response = chat_with_role(request.message, [])
            
            # 检查是否是错误信息
            if response.startswith("❌") or response.startswith("⚠️"):
                return role_play_pb2.ChatResponse(
                    success=False,
                    response="",
                    error=response
                )
            
            return role_play_pb2.ChatResponse(
                success=True,
                response=response,
                error=""
            )
        except Exception as e:
            return role_play_pb2.ChatResponse(
                success=False,
                response="",
                error=f"对话失败: {str(e)}"
            )
    
    def ResetConversation(self, request, context):
        """重置对话"""
        try:
            # 调用原有的重置函数
            reset_conversation()
            
            return role_play_pb2.ResetResponse(
                success=True,
                message="对话已重置"
            )
        except Exception as e:
            return role_play_pb2.ResetResponse(
                success=False,
                message=f"重置对话失败: {str(e)}"
            )
    
    def GetPresetRoles(self, request, context):
        """获取预设角色列表"""
        try:
            roles = []
            for emoji_name, role_data in PRESET_ROLES.items():
                # 从"🧙‍♂️ 智慧导师"这样的字符串中提取emoji和名称
                parts = emoji_name.split(' ', 1)
                emoji = parts[0] if len(parts) > 1 else ""
                name = role_data.get("name", "")
                description = role_data.get("description", "")
                
                roles.append(role_play_pb2.PresetRole(
                    name=name,
                    description=description,
                    emoji=emoji
                ))
            
            return role_play_pb2.GetPresetRolesResponse(roles=roles)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"获取预设角色失败: {str(e)}")
            return role_play_pb2.GetPresetRolesResponse()

def serve():
    """启动gRPC服务器"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    role_play_pb2_grpc.add_RolePlayServiceServicer_to_server(
        RolePlayServiceServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("AI角色扮演gRPC服务器已启动，监听端口50051...")
    print("按Ctrl+C停止服务器")
    
    try:
        while True:
            time.sleep(86400)  # 一天
    except KeyboardInterrupt:
        server.stop(0)
        print("\n服务器已停止")

if __name__ == '__main__':
    serve()