"""
简单的 LangGraph 智能体应用
演示使用 LangGraph 构建基础智能体工作流
"""

from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import operator
import os
import sys

# 加载环境变量
env_loaded = load_dotenv()

# 检查 .env 文件是否成功加载
if env_loaded:
    print("✅ 成功读取 .env 文件")
else:
    print("⚠️  未找到 .env 文件或文件为空")
    print("提示：请将 .env.example 复制为 .env 并配置 API Key")

# 初始化大模型
# 优先使用智谱 AI（免费），如果没有配置则使用 OpenAI
zhipu_api_key = os.getenv("ZHIPU_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# 显示检测到的 API Key 配置状态
print("\n" + "-" * 50)
print("API Key 配置状态：")
if zhipu_api_key:
    # 只显示部分 Key，保护隐私
    masked_key = zhipu_api_key[:8] + "***" + zhipu_api_key[-4:] if len(zhipu_api_key) > 12 else "***"
    print(f"  ZHIPU_API_KEY: {masked_key}")
else:
    print("  ZHIPU_API_KEY: ❌ 未配置")

if openai_api_key:
    masked_key = openai_api_key[:8] + "***" + openai_api_key[-4:] if len(openai_api_key) > 12 else "***"
    print(f"  OPENAI_API_KEY: {masked_key}")
else:
    print("  OPENAI_API_KEY: ❌ 未配置")
print("-" * 50)

llm = None
api_provider = None

if zhipu_api_key:
    # 使用智谱 AI（免费）
    api_provider = "智谱 AI"
    print(f"\n📌 选择使用: {api_provider} (glm-4-flash)\n")
    llm = ChatOpenAI(
        model="glm-4-flash",
        temperature=0.7,
        api_key=zhipu_api_key,  # type: ignore
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    )
elif openai_api_key:
    # 使用 OpenAI
    api_provider = "OpenAI"
    print(f"\n📌 选择使用: {api_provider} (gpt-3.5-turbo)\n")
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=openai_api_key  # type: ignore
    )
else:
    print("\n⚠️  未检测到任何可用的 API Key\n")
    api_provider = None


def test_llm_connection():
    """测试大模型连接是否正常"""
    if llm is None:
        print("\n" + "=" * 60)
        print("❌ 未配置 API Key")
        print("=" * 60)
        print("\n请按照以下步骤配置：")
        print("\n【推荐】智谱 AI（免费）：")
        print("  1. 访问：https://open.bigmodel.cn/")
        print("  2. 注册并登录")
        print("  3. 获取 API Key：个人中心 -> API Keys")
        print("  4. 在 .env 文件中配置：ZHIPU_API_KEY=你的Key")
        print("\nOpenAI（付费，国内访问困难）：")
        print("  1. 访问：https://platform.openai.com/")
        print("  2. 获取 API Key")
        print("  3. 在 .env 文件中配置：OPENAI_API_KEY=你的Key")
        print("\n" + "=" * 60)
        return False
    
    print(f"\n正在测试 {api_provider} 连接...")
    
    try:
        # 发送一个简单的测试请求
        response = llm.invoke("你好")
        if response and response.content:
            print(f"✅ {api_provider} 连接成功！")
            print(f"测试响应：{str(response.content)[:50]}...\n")
            return True
        else:
            print(f"⚠️  {api_provider} 响应异常")
            return False
    except Exception as e:
        error_msg = str(e)
        print(f"\n" + "=" * 60)
        print(f"❌ {api_provider} 连接失败")
        print("=" * 60)
        
        if "Connection error" in error_msg or "连接" in error_msg:
            if api_provider == "OpenAI":
                print("\n原因：OpenAI API 在国内无法直接访问")
                print("\n解决方案：")
                print("  1. 【推荐】切换到智谱 AI（免费且快速）")
                print("     - 访问：https://open.bigmodel.cn/")
                print("     - 获取 API Key 后配置到 .env 文件")
                print("     - 配置项：ZHIPU_API_KEY=你的Key")
                print("  2. 使用代理/VPN 访问 OpenAI")
            else:
                print(f"\n网络连接错误，请检查：")
                print("  1. 网络连接是否正常")
                print("  2. API Key 是否正确")
                print("  3. 是否有防火墙拦截")
        elif "API key" in error_msg or "Incorrect" in error_msg or "Invalid" in error_msg:
            print(f"\nAPI Key 错误，请检查：")
            print(f"  1. .env 文件中的 API Key 是否正确")
            print(f"  2. API Key 是否已过期或被删除")
            print(f"  3. 重新获取 API Key 并更新配置")
        else:
            print(f"\n错误详情：{error_msg}")
        
        print("\n" + "=" * 60)
        return False


# 定义状态结构
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    next_step: str
    result: str


# 定义节点函数
def process_input(state: AgentState) -> AgentState:
    """处理初始输入"""
    print("正在处理输入...")
    messages = state.get("messages", [])
    
    if messages:
        last_message = messages[-1]
        print(f"收到消息: {last_message}")
        
        # 简单的决策逻辑
        if "hello" in last_message.lower():
            state["next_step"] = "greet"
        elif "help" in last_message.lower():
            state["next_step"] = "provide_help"
        else:
            state["next_step"] = "general_response"
    
    return state


def greet_user(state: AgentState) -> AgentState:
    """向用户问候"""
    print("正在问候用户...")
    state["result"] = "你好！我是你的 LangGraph 智能体。有什么可以帮助你的吗？"
    state["next_step"] = "end"
    return state


def provide_help(state: AgentState) -> AgentState:
    """提供帮助信息"""
    print("正在提供帮助...")
    state["result"] = """
    我是一个简单的 LangGraph 智能体。以下是我能做的事情：
    - 当你向我问候时，我会打招呼
    - 当你需要帮助时，我会提供帮助信息
    - 对其他输入，我会给出一般性回复
    
    试着说：'你好'、'帮助' 或其他任何内容！
    """
    state["next_step"] = "end"
    return state


def general_response(state: AgentState) -> AgentState:
    """提供一般性回复（使用大模型）"""
    messages = state.get("messages", [])
    last_message = messages[-1] if messages else "无内容"
    
    # 检查是否配置了大模型
    if llm is None:
        state["result"] = f"收到消息：'{last_message}'\n\n⚠️ 未配置 API Key，无法使用大模型。\n请在 .env 文件中配置 ZHIPU_API_KEY 或 OPENAI_API_KEY"
        state["next_step"] = "end"
        return state
    
    print("正在使用大模型生成回复...")
    
    try:
        # 使用大模型生成回复
        response = llm.invoke(f"请用友好、简洁的方式回答用户的问题：{last_message}")
        result_content = str(response.content) if response.content else "抱歉，我无法生成回复。"
        state["result"] = result_content
    except Exception as e:
        # 如果大模型调用失败，返回错误信息
        error_msg = str(e)
        if "Connection error" in error_msg or "连接" in error_msg:
            state["result"] = f"❌ 网络连接失败\n\n可能的原因：\n1. OpenAI API 在国内无法直接访问，建议使用智谱 AI（免费）\n2. 请配置 ZHIPU_API_KEY 来使用免费的国内大模型\n\n详细错误：{error_msg}"
        else:
            state["result"] = f"抱歉，我在处理你的消息时遇到了问题：{error_msg}\n请检查你的 API Key 配置是否正确。"
    
    state["next_step"] = "end"
    return state


def route_next(state: AgentState) -> str:
    """决定下一个要访问的节点"""
    next_step = state.get("next_step", "end")
    
    if next_step == "greet":
        return "greet"
    elif next_step == "provide_help":
        return "help"
    elif next_step == "general_response":
        return "general"
    else:
        return "end"


# 构建图
def create_agent_graph():
    """创建并编译智能体图"""
    workflow = StateGraph(AgentState)
    
    # 添加节点
    workflow.add_node("process", process_input)
    workflow.add_node("greet", greet_user)
    workflow.add_node("help", provide_help)
    workflow.add_node("general", general_response)
    
    # 设置入口点
    workflow.set_entry_point("process")
    
    # 添加条件边
    workflow.add_conditional_edges(
        "process",
        route_next,
        {
            "greet": "greet",
            "help": "help",
            "general": "general",
            "end": END
        }
    )
    
    # 添加到结束节点的边
    workflow.add_edge("greet", END)
    workflow.add_edge("help", END)
    workflow.add_edge("general", END)
    
    # 编译图
    app = workflow.compile()
    return app


def run_demo():
    """使用预定义输入运行演示"""
    print("=" * 50)
    print("简单 LangGraph 智能体 - 演示模式")
    print("=" * 50)
    
    # 测试连接
    if not test_llm_connection():
        print("\n⚠️  大模型功能不可用，仅演示基础功能\n")
    
    # 创建智能体
    agent = create_agent_graph()
    
    # 测试示例
    test_inputs = [
        "你好！",
        "我需要帮助",
        "今天天气怎么样？"
    ]
    
    for user_input in test_inputs:
        print(f"\n{'=' * 50}")
        print(f"用户: {user_input}")
        print("-" * 50)
        
        # 运行智能体
        result = agent.invoke({
            "messages": [user_input],
            "next_step": "",
            "result": ""
        })
        
        print("-" * 50)
        print(f"智能体: {result['result']}")
    
    print(f"\n{'=' * 50}")
    print("演示完成！")
    print("=" * 50)


def run_interactive():
    """运行交互模式，用户可以输入消息"""
    print("=" * 50)
    print("简单 LangGraph 智能体 - 交互模式")
    print("=" * 50)
    
    # 测试连接
    if not test_llm_connection():
        print("\n请先配置 API Key 后再使用交互模式")
        sys.exit(1)
    
    print("输入 'quit'、'exit' 或 'q' 退出\n")
    
    # 创建智能体
    agent = create_agent_graph()
    
    while True:
        # 获取用户输入
        user_input = input("你: ").strip()
        
        # 检查退出命令
        if user_input.lower() in ['quit', 'exit', 'q', '退出', '结束']:
            print("\n再见！")
            break
        
        if not user_input:
            continue
        
        # 运行智能体
        print("-" * 50)
        result = agent.invoke({
            "messages": [user_input],
            "next_step": "",
            "result": ""
        })
        
        print(f"智能体: {result['result']}")
        print()


def main():
    """运行智能体的主函数"""
    import sys
    
    # 检查命令行参数
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        run_interactive()
    else:
        run_demo()


if __name__ == "__main__":
    main()
