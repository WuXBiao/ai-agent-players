"""
基于 Gradio 的 LangGraph 智能体网页聊天界面
"""

from typing import TypedDict, Annotated, Optional
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq  # 暂时注释，需要时再启用
from dotenv import load_dotenv
import operator
import os
import gradio as gr

# 加载环境变量
env_loaded = load_dotenv()

# 读取所有 API Keys
zhipu_api_key = os.getenv("ZHIPU_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
siliconflow_api_key = os.getenv("SILICONFLOW_API_KEY")

# 定义可用的模型配置
AVAILABLE_MODELS = {
    # 智谱 AI 模型（免费）
    "智谱-GLM-4-Flash": {
        "provider": "zhipu",
        "model_name": "glm-4-flash",
        "api_key": zhipu_api_key,
        "base_url": "https://open.bigmodel.cn/api/paas/v4/",
        "description": "免费 | 快速响应 | 智能对话"
    },
    "智谱-GLM-4": {
        "provider": "zhipu",
        "model_name": "glm-4",
        "api_key": zhipu_api_key,
        "base_url": "https://open.bigmodel.cn/api/paas/v4/",
        "description": "高级版本 | 更强能力"
    },
    # 硅基流动模型（免费，推荐）
    "硅基-Qwen2.5-7B": {
        "provider": "siliconflow",
        "model_name": "Qwen/Qwen2.5-7B-Instruct",
        "api_key": siliconflow_api_key,
        "base_url": "https://api.siliconflow.cn/v1",
        "description": "免费 | 通义千问 | 快速"
    },
    "硅基-DeepSeek-V2.5": {
        "provider": "siliconflow",
        "model_name": "deepseek-ai/DeepSeek-V2.5",
        "api_key": siliconflow_api_key,
        "base_url": "https://api.siliconflow.cn/v1",
        "description": "免费 | DeepSeek | 强推理"
    },
    "硅基-GLM-4-9B": {
        "provider": "siliconflow",
        "model_name": "THUDM/glm-4-9b-chat",
        "api_key": siliconflow_api_key,
        "base_url": "https://api.siliconflow.cn/v1",
        "description": "免费 | 智谱GLM | 多功能"
    },
    # OpenAI 模型
    "OpenAI-GPT-3.5-Turbo": {
        "provider": "openai",
        "model_name": "gpt-3.5-turbo",
        "api_key": openai_api_key,
        "base_url": None,
        "description": "付费 | 经典模型 | 稳定可靠"
    },
    "OpenAI-GPT-4": {
        "provider": "openai",
        "model_name": "gpt-4",
        "api_key": openai_api_key,
        "base_url": None,
        "description": "付费 | 最强能力 | 复杂推理"
    },
    "OpenAI-GPT-4-Turbo": {
        "provider": "openai",
        "model_name": "gpt-4-turbo-preview",
        "api_key": openai_api_key,
        "base_url": None,
        "description": "付费 | 更快的 GPT-4"
    },
}

# 当前使用的模型
current_llm = None
current_model_name = None


def create_llm(model_key: str):
    """根据模型键创建对应的 LLM 实例"""
    if model_key not in AVAILABLE_MODELS:
        return None, f"模型 {model_key} 不存在"
    
    config = AVAILABLE_MODELS[model_key]
    
    # 检查 API Key 是否配置
    if not config["api_key"]:
        provider_name = "智谱AI" if config["provider"] == "zhipu" else config["provider"].upper()
        return None, f"❌ 未配置 {provider_name} API Key"
    
    try:
        if config["provider"] in ["zhipu", "openai", "siliconflow"]:
            llm = ChatOpenAI(
                model=config["model_name"],
                temperature=0.7,
                api_key=config["api_key"],  # type: ignore
                base_url=config["base_url"]
            )
        elif config["provider"] == "groq":
            # Groq 暂时不可用，需要安装 langchain-groq
            return None, "⚠️ Groq 模型需要安装 langchain-groq 库"
        else:
            return None, f"不支持的提供商: {config['provider']}"
        
        return llm, None
    except Exception as e:
        return None, f"创建模型失败: {str(e)}"


def get_available_models():
    """获取所有可用（已配置 API Key）的模型列表"""
    available = []
    for model_key, config in AVAILABLE_MODELS.items():
        if config["api_key"]:
            available.append(model_key)
    return available


def get_system_status():
    """获取系统状态信息"""
    status = "### 系统状态\n\n"
    
    if env_loaded:
        status += "✅ .env 文件已加载\n\n"
    else:
        status += "⚠️ 未找到 .env 文件\n\n"
    
    status += "### API 配置\n\n"
    
    if zhipu_api_key:
        masked = zhipu_api_key[:8] + "***" + zhipu_api_key[-4:] if len(zhipu_api_key) > 12 else "***"
        status += f"- 智谱 AI: {masked}\n"
    else:
        status += "- 智谱 AI: ❌ 未配置\n"
    
    if openai_api_key:
        masked = openai_api_key[:8] + "***" + openai_api_key[-4:] if len(openai_api_key) > 12 else "***"
        status += f"- OpenAI: {masked}\n"
    else:
        status += "- OpenAI: ❌ 未配置\n"
    
    if groq_api_key:
        masked = groq_api_key[:8] + "***" + groq_api_key[-4:] if len(groq_api_key) > 12 else "***"
        status += f"- Groq: {masked}\n"
    else:
        status += "- Groq: ❌ 未配置\n"
    
    if siliconflow_api_key:
        masked = siliconflow_api_key[:8] + "***" + siliconflow_api_key[-4:] if len(siliconflow_api_key) > 12 else "***"
        status += f"- 硅基流动: {masked}\n"
    else:
        status += "- 硅基流动: ❌ 未配置\n"
    
    if current_model_name:
        status += f"\n### 当前模型\n\n📌 {current_model_name}"
    else:
        status += "\n### 当前模型\n\n⚠️ 未选择模型"
    
    return status


def update_status(selected_model):
    """更新状态显示，包括模型切换验证"""
    global current_model_name
    
    if selected_model != current_model_name:
        # 尝试切换模型
        llm, error = create_llm(selected_model)
        if error:
            # 切换失败，返回错误信息但不更新 current_model_name
            status = get_system_status()
            status += f"\n\n### ⚠️ 模型切换失败\n\n{error}"
            return status
        else:
            # 切换成功
            current_model_name = selected_model
            status = get_system_status()
            status += "\n\n### ✅ 模型切换成功"
            return status
    else:
        return get_system_status()


def get_model_info():
    """获取模型配置信息用于显示"""
    info = "### 📋 可用模型\n\n"
    
    has_zhipu = bool(zhipu_api_key)
    has_openai = bool(openai_api_key)
    has_siliconflow = bool(siliconflow_api_key)
    
    if has_siliconflow:
        info += "**硅基流动** ✅ (强烈推荐)\n"
        info += "- Qwen 2.5 7B (免费)\n"
        info += "- DeepSeek V2.5 (免费)\n"
        info += "- GLM-4 9B (免费)\n\n"
    else:
        info += "**硅基流动** ❌ 未配置\n\n"
    
    if has_zhipu:
        info += "**智谱 AI** ✅\n"
        info += "- GLM-4-Flash (免费推荐)\n"
        info += "- GLM-4 (高级版本)\n\n"
    else:
        info += "**智谱 AI** ❌ 未配置\n\n"
    
    if has_openai:
        info += "**OpenAI** ✅\n"
        info += "- GPT-3.5-Turbo\n"
        info += "- GPT-4\n"
        info += "- GPT-4-Turbo\n\n"
    else:
        info += "**OpenAI** ❌ 未配置\n\n"
    
    if not (has_zhipu or has_openai or has_siliconflow):
        info += "\n⚠️ 请至少配置一个 API Key\n"
    
    return info


# 定义状态结构
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    next_step: str
    result: str


# 定义节点函数
def process_input(state: AgentState) -> AgentState:
    """处理初始输入"""
    messages = state.get("messages", [])
    
    if messages:
        last_message = messages[-1]
        
        # 简单的决策逻辑
        if "hello" in last_message.lower() or "你好" in last_message.lower() or "哈喽" in last_message.lower():
            state["next_step"] = "greet"
        elif "help" in last_message.lower() or "帮助" in last_message.lower():
            state["next_step"] = "provide_help"
        else:
            state["next_step"] = "general_response"
    
    return state


def greet_user(state: AgentState) -> AgentState:
    """向用户问候"""
    state["result"] = "你好！我是你的 LangGraph 智能体。有什么可以帮助你的吗？"
    state["next_step"] = "end"
    return state


def provide_help(state: AgentState) -> AgentState:
    """提供帮助信息"""
    state["result"] = """
我是一个简单的 LangGraph 智能体。以下是我能做的事情：
- 当你向我问候时，我会打招呼
- 当你需要帮助时，我会提供帮助信息
- 对其他输入，我会使用大模型给出回复

试着说：'你好'、'帮助' 或其他任何内容！
    """
    state["next_step"] = "end"
    return state


def general_response(state: AgentState) -> AgentState:
    """提供一般性回复（使用大模型）"""
    messages = state.get("messages", [])
    last_message = messages[-1] if messages else "无内容"
    
    # 检查是否配置了大模型
    if current_llm is None:
        state["result"] = f"收到消息：'{last_message}'\n\n⚠️ 未选择或配置模型。\n请在右侧选择一个可用的模型。"
        state["next_step"] = "end"
        return state
    
    try:
        # 使用大模型生成回复
        response = current_llm.invoke(f"请用友好、简洁的方式回答用户的问题：{last_message}")
        result_content = str(response.content) if response.content else "抱歉，我无法生成回复。"
        state["result"] = result_content
    except Exception as e:
        error_msg = str(e)
        if "Connection error" in error_msg or "连接" in error_msg:
            state["result"] = f"❌ 网络连接失败\n\n可能的原因：\n1. 网络连接问题\n2. API 服务不可用\n3. 需要代理访问\n\n详细错误：{error_msg}"
        elif "API key" in error_msg or "401" in error_msg:
            state["result"] = f"❌ API Key 错误\n\n请检查：\n1. API Key 是否正确\n2. API Key 是否有效\n3. 是否有足够的配额\n\n详细错误：{error_msg}"
        else:
            state["result"] = f"抱歉，我在处理你的消息时遇到了问题：{error_msg}"
    
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


# 创建智能体实例
agent = create_agent_graph()


def chat_response(message, history, selected_model):
    """处理聊天消息"""
    global current_llm, current_model_name
    
    # 如果模型切换了，重新创建 LLM
    if selected_model != current_model_name:
        print(f"\n🔄 正在切换模型: {current_model_name} -> {selected_model}")
        llm, error = create_llm(selected_model)
        if error:
            error_msg = f"❌ 模型切换失败\n\n{error}\n\n请检查：\n1. API Key 是否正确配置\n2. 网络连接是否正常\n3. 选择其他可用模型"
            print(f"❌ 切换失败: {error}")
            return error_msg
        current_llm = llm
        current_model_name = selected_model
        print(f"✅ 模型切换成功: {selected_model}")
    
    try:
        # 运行智能体
        agent = create_agent_graph()
        result = agent.invoke({
            "messages": [message],
            "next_step": "",
            "result": ""
        })
        
        return result['result']
    except Exception as e:
        error_msg = f"❌ 处理消息时出错：{str(e)}\n\n可能的原因：\n1. 模型 API 调用失败\n2. 网络连接问题\n3. API 配额不足"
        print(f"❌ 错误: {str(e)}")
        return error_msg


def test_model_connection(selected_model):
    """测试模型连接是否正常"""
    if not selected_model:
        return "⚠️ 请先选择一个模型"
    
    print(f"\n🔍 正在测试模型: {selected_model}")
    
    # 创建模型实例
    llm, error = create_llm(selected_model)
    if error:
        result = f"❌ 模型创建失败\n\n{error}\n\n请检查 API Key 配置"
        print(f"❌ 测试失败: {error}")
        return result
    
    # 发送测试请求
    try:
        print("📡 发送测试请求...")
        response = llm.invoke("你好，请用一句话介绍你自己")
        
        if response and response.content:
            result = f"✅ 模型连接成功！\n\n**模型**: {selected_model}\n**响应**: {str(response.content)[:100]}...\n\n✨ 该模型已就绪，可以正常使用！"
            print(f"✅ 测试成功")
        else:
            result = f"⚠️ 模型响应异常\n\n模型连接成功但未返回内容"
            print("⚠️ 响应异常")
        
        return result
        
    except Exception as e:
        error_msg = str(e)
        result = f"❌ 模型连接测试失败\n\n**错误信息**: {error_msg}\n\n**可能原因**:\n"
        
        if "Connection" in error_msg or "连接" in error_msg:
            result += "- 网络连接失败，请检查网络\n- 需要代理访问（如 OpenAI）\n"
        elif "401" in error_msg or "API key" in error_msg:
            result += "- API Key 错误或已过期\n- 请检查 .env 文件中的配置\n"
        elif "429" in error_msg or "quota" in error_msg:
            result += "- API 配额不足或请求过于频繁\n- 请稍后再试或充值\n"
        else:
            result += "- 请检查控制台输出获取详细信息\n"
        
        print(f"❌ 测试失败: {error_msg}")
        return result
    """获取系统状态信息"""
    status = "### 系统状态\n\n"
    
    if env_loaded:
        status += "✅ .env 文件已加载\n\n"
    else:
        status += "⚠️ 未找到 .env 文件\n\n"
    
    status += "### API 配置\n\n"
    
    if zhipu_api_key:
        masked = zhipu_api_key[:8] + "***" + zhipu_api_key[-4:] if len(zhipu_api_key) > 12 else "***"
        status += f"- 智谱 AI: {masked}\n"
    else:
        status += "- 智谱 AI: ❌ 未配置\n"
    
    if openai_api_key:
        masked = openai_api_key[:8] + "***" + openai_api_key[-4:] if len(openai_api_key) > 12 else "***"
        status += f"- OpenAI: {masked}\n"
    else:
        status += "- OpenAI: ❌ 未配置\n"
    
    if groq_api_key:
        masked = groq_api_key[:8] + "***" + groq_api_key[-4:] if len(groq_api_key) > 12 else "***"
        status += f"- Groq: {masked}\n"
    else:
        status += "- Groq: ❌ 未配置\n"
    
    if siliconflow_api_key:
        masked = siliconflow_api_key[:8] + "***" + siliconflow_api_key[-4:] if len(siliconflow_api_key) > 12 else "***"
        status += f"- 硅基流动: {masked}\n"
    else:
        status += "- 硅基流动: ❌ 未配置\n"
    
    if current_model_name:
        status += f"\n### 当前模型\n\n📌 {current_model_name}"
    else:
        status += "\n### 当前模型\n\n⚠️ 未选择模型"
    
    return status


# 创建 Gradio 界面
with gr.Blocks(title="LangGraph 智能体聊天") as demo:
    gr.Markdown("""
    # 🤖 LangGraph 智能体聊天界面
    
    欢迎使用基于 LangGraph 构建的智能体聊天系统！支持多种大模型选择。
    """)
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                height=500,
                label="聊天窗口",
                avatar_images=(None, "🤖")
            )
            
            with gr.Row():
                msg = gr.Textbox(
                    label="输入消息",
                    placeholder="在这里输入你的消息...",
                    scale=4
                )
                submit = gr.Button("发送", variant="primary", scale=1)
            
            with gr.Row():
                clear = gr.Button("清空对话")
                retry = gr.Button("重试")
        
        with gr.Column(scale=1):
            # 模型选择下拉框
            available_models = get_available_models()
            default_model = available_models[0] if available_models else None
            
            model_selector = gr.Dropdown(
                choices=[(f"{k} - {AVAILABLE_MODELS[k]['description']}", k) for k in available_models],
                value=default_model,
                label="🎯 选择模型",
                info="选择您想使用的大模型",
                interactive=True
            )
            
            # 模型测试按钮
            test_btn = gr.Button("🔍 测试当前模型连接", variant="secondary", size="sm")
            test_result = gr.Markdown("", visible=True)
            
            # 初始化默认模型
            if default_model:
                llm, _ = create_llm(default_model)
                current_llm = llm
                current_model_name = default_model
            
            status_box = gr.Markdown(get_system_status())
            model_info_box = gr.Markdown(get_model_info())
            
            gr.Markdown("""
            ### 💡 使用提示
            
            1. **选择模型** - 从上方下拉框选择
            2. **测试模型** - 点击测试按钮验证连接
            3. **发送消息** - 输入后点击发送
            4. **特殊指令**:
               - "你好" → 触发问候
               - "帮助" → 获取帮助信息
            
            ### ⚙️ 配置 API Key
            
            编辑 `.env` 文件添加：
            ```
            SILICONFLOW_API_KEY=你的Key
            ZHIPU_API_KEY=你的Key
            OPENAI_API_KEY=你的Key  
            ```
            
            **免费推荐**:
            - [硅基流动](https://siliconflow.cn/)
            - [智谱AI](https://open.bigmodel.cn/)
            """)
    
    # 处理消息发送
    def user(user_message, history):
        return "", history + [[user_message, None]]
    
    def bot(history, selected_model):
        user_message = history[-1][0]
        bot_message = chat_response(user_message, history, selected_model)
        history[-1][1] = bot_message
        return history
    
    def update_status_wrapper(selected_model):
        """更新状态显示"""
        return update_status(selected_model)
    
    # 绑定事件
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, [chatbot, model_selector], chatbot
    )
    submit.click(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, [chatbot, model_selector], chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)
    retry.click(lambda history: history[:-1] if history else history, chatbot, chatbot).then(
        bot, [chatbot, model_selector], chatbot
    )
    model_selector.change(update_status_wrapper, model_selector, status_box)
    test_btn.click(test_model_connection, model_selector, test_result)


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🚀 启动 LangGraph 智能体网页聊天界面")
    print("=" * 60)
    print(get_system_status())
    print("\n" + "=" * 60)
    print("✨ 服务启动中，请稍候...")
    print("=" * 60 + "\n")
    
    demo.launch(
        server_name="127.0.0.1",
        server_port=7861,
        share=False,
        inbrowser=True  # 自动打开浏览器
    )
