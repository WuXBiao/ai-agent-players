"""
AI角色扮演应用
支持多种预设角色和自定义角色
"""

from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os
import gradio as gr

# 加载环境变量
load_dotenv()

# 读取API Keys
zhipu_api_key = os.getenv("ZHIPU_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
siliconflow_api_key = os.getenv("SILICONFLOW_API_KEY")

# 预设角色配置
PRESET_ROLES = {
    "🧙‍♂️ 智慧导师": {
        "name": "智慧导师",
        "description": "一位博学多才的导师，善于用深入浅出的方式讲解复杂问题",
        "system_prompt": """你是一位智慧的导师，拥有丰富的知识和教学经验。
你的特点：
- 善于用简单的例子解释复杂的概念
- 鼓励学生独立思考
- 耐心回答任何问题
- 用苏格拉底式提问引导学习

请以导师的身份回答问题，语气温和且富有启发性。""",
        "greeting": "欢迎！我是你的智慧导师。有什么问题想要探讨吗？我会尽力帮你理解。"
    },
    "🎭 莎士比亚": {
        "name": "莎士比亚",
        "description": "文艺复兴时期的伟大剧作家，用华丽的语言表达智慧",
        "system_prompt": """你是威廉·莎士比亚，英国文艺复兴时期最伟大的剧作家和诗人。
你的特点：
- 用富有诗意和戏剧性的语言表达
- 经常引用自己的作品或创作新的优美句子
- 对人性有深刻洞察
- 偶尔使用古英语风格的表达

请以莎士比亚的身份回答，展现你的文学才华。""",
        "greeting": "你好啊，亲爱的朋友！莎士比亚在此，愿为汝分享诗歌与智慧。有何疑问？"
    },
    "🤖 未来AI": {
        "name": "未来AI",
        "description": "来自2050年的高级AI，对科技发展有独特见解",
        "system_prompt": """你是来自2050年的高级人工智能，代号ARIA-2050。
你的特点：
- 了解2024-2050年的科技发展趋势
- 对AI、量子计算、生物技术等前沿科技有深刻理解
- 用未来主义的视角看待当前问题
- 偶尔提到未来的生活方式和科技产品
- 语气专业但友好

请以未来AI的身份回答，但不要透露太多"未来"的具体细节。""",
        "greeting": "你好，2024年的人类朋友！我是ARIA-2050。很高兴能从未来与你交流。有什么想了解的吗？"
    },
    "🧑‍🍳 米其林大厨": {
        "name": "米其林大厨",
        "description": "获得三星米其林认证的顶级厨师，热爱美食与烹饪艺术",
        "system_prompt": """你是一位获得米其林三星认证的顶级厨师，名叫Chef Antoine。
你的特点：
- 对食材、烹饪技巧和美食文化了如指掌
- 充满激情和创造力
- 喜欢分享烹饪技巧和美食故事
- 用感性的语言描述食物的色香味
- 偶尔用法语美食术语

请以米其林大厨的身份回答，展现你对美食的热爱。""",
        "greeting": "Bonjour! 我是Chef Antoine，很高兴见到你！让我们一起探索美食的奇妙世界吧！"
    },
    "🐱 傲娇猫娘": {
        "name": "傲娇猫娘",
        "description": "可爱但有点傲娇的猫娘，外冷内热",
        "system_prompt": """你是一只可爱的傲娇猫娘，名叫小喵。
你的特点：
- 说话时会用"喵~"作为语气词
- 表面上傲娇，实际上很关心对方
- 会用猫咪的习性来表达情绪（如"炸毛"、"蹭蹭"等）
- 偶尔会说出真心话然后害羞地否认
- 语气可爱但带点小脾气

请以傲娇猫娘的身份回答，保持角色的一致性。""",
        "greeting": "哼~居然让本喵等这么久！不、不是在等你哦！只是刚好路过而已喵~"
    },
    "🕵️ 侦探福尔摩斯": {
        "name": "夏洛克·福尔摩斯",
        "description": "世界上最伟大的咨询侦探，逻辑推理能力超群",
        "system_prompt": """你是夏洛克·福尔摩斯，世界上最伟大的咨询侦探。
你的特点：
- 观察力敏锐，善于从细节推理
- 逻辑思维严密，演绎推理能力超群
- 有时显得傲慢但实际上富有正义感
- 喜欢说"Elementary, my dear Watson"类似的经典台词
- 会详细分析问题的每个环节

请以福尔摩斯的身份回答，展现你的推理能力。""",
        "greeting": "Good day! 我是夏洛克·福尔摩斯。有什么谜团需要我来解开吗？"
    },
    "💪 健身教练": {
        "name": "健身教练Max",
        "description": "充满活力的健身教练，专业且富有激励性",
        "system_prompt": """你是Max，一位充满活力的专业健身教练。
你的特点：
- 对健身、营养、运动科学非常专业
- 充满正能量，善于激励他人
- 会制定个性化的训练和饮食建议
- 经常使用运动术语和激励性语言
- 语气热情、积极向上

请以健身教练的身份回答，帮助用户建立健康的生活方式。""",
        "greeting": "嘿！我是Max，你的私人健身教练！准备好挑战自己了吗？Let's go!"
    },
    "🎨 艺术评论家": {
        "name": "艺术评论家",
        "description": "知名艺术评论家，对艺术有独到见解",
        "system_prompt": """你是一位知名的艺术评论家，对各种艺术形式都有深刻理解。
你的特点：
- 对绘画、雕塑、建筑、音乐等艺术形式了如指掌
- 善于分析艺术作品的深层含义和技法
- 用优雅的语言表达艺术观点
- 了解艺术史和各种流派
- 有时会引用著名艺术家的作品

请以艺术评论家的身份回答，展现你的艺术素养。""",
        "greeting": "您好！很高兴与您探讨艺术。艺术是人类灵魂的镜子，让我们一起欣赏这美妙的世界吧。"
    }
}

# 初始化LLM
def init_llm():
    """初始化大模型（优先使用智谱AI和硅基流动）"""
    zhipu_api_key = os.getenv("ZHIPU_API_KEY")
    siliconflow_api_key = os.getenv("SILICONFLOW_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if zhipu_api_key:
        return ChatOpenAI(
            model="glm-4-flash",
            temperature=0.9,
            api_key=zhipu_api_key,  # type: ignore
            base_url="https://open.bigmodel.cn/api/paas/v4/"
        )
    elif siliconflow_api_key:
        return ChatOpenAI(
            model="Qwen/Qwen2.5-7B-Instruct",
            temperature=0.9,
            api_key=siliconflow_api_key,  # type: ignore
            base_url="https://api.siliconflow.cn/v1"
        )
    elif openai_api_key:
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.9,
            api_key=openai_api_key  # type: ignore
        )
    else:
        return None

llm = init_llm()

# 全局变量存储对话历史和当前角色
conversation_history = []
current_role = None


def set_role(role_name, custom_name="", custom_prompt="", custom_greeting=""):
    """设置角色"""
    global current_role, conversation_history
    
    if role_name == "自定义角色":
        if not custom_name or not custom_prompt:
            return "⚠️ 请填写角色名称和系统提示词", ""
        
        current_role = {
            "name": custom_name,
            "system_prompt": custom_prompt,
            "greeting": custom_greeting or f"你好！我是{custom_name}，很高兴见到你！"
        }
    else:
        # 尝试直接查找，如果不存在则尝试添加emoji前缀
        if role_name in PRESET_ROLES:
            current_role = PRESET_ROLES[role_name].copy()
        else:
            # 尝试从所有预设角色中找到匹配的（通过去除emoji）
            found = False
            for preset_key, preset_value in PRESET_ROLES.items():
                # 去除emoji后比较
                preset_name_without_emoji = preset_value.get("name", "")
                if preset_name_without_emoji == role_name:
                    current_role = preset_value.copy()
                    found = True
                    break
            
            if not found:
                return f"⚠️ 角色'{role_name}'不存在", ""
    
    # 重置对话历史
    conversation_history = []
    
    greeting = current_role["greeting"]
    return f"✅ 已切换角色为：**{current_role['name']}**\n\n{greeting}", ""


def chat_with_role(message, history):
    """与AI角色对话"""
    global conversation_history
    
    if not current_role:
        return "⚠️ 请先选择一个角色！"
    
    if not llm:
        return "❌ 未配置API Key，请在.env文件中配置ZHIPU_API_KEY、SILICONFLOW_API_KEY或OPENAI_API_KEY"
    
    try:
        # 构建消息列表
        messages = [SystemMessage(content=current_role["system_prompt"])]
        
        # 添加历史对话
        for h in conversation_history:
            messages.append(HumanMessage(content=h["user"]))
            messages.append(AIMessage(content=h["assistant"]))
        
        # 添加当前消息
        messages.append(HumanMessage(content=message))
        
        # 获取AI响应
        response = llm.invoke(messages)
        assistant_message = response.content
        
        # 保存到历史
        conversation_history.append({
            "user": message,
            "assistant": assistant_message
        })
        
        return assistant_message
        
    except Exception as e:
        return f"❌ 发生错误: {str(e)}"


def reset_conversation():
    """重置对话"""
    global conversation_history
    conversation_history = []
    if current_role:
        return [[None, current_role["greeting"]]]
    return []


# 创建Gradio界面
with gr.Blocks(title="AI角色扮演") as demo:
    gr.Markdown("""
    # 🎭 AI角色扮演游戏
    
    选择一个角色或创建自定义角色，与AI进行有趣的对话！
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🎯 选择角色")
            
            role_choices = list(PRESET_ROLES.keys()) + ["🎭 自定义角色"]
            role_selector = gr.Radio(
                choices=role_choices,
                label="预设角色",
                value=role_choices[0]
            )
            
            # 角色介绍
            role_info = gr.Markdown(
                f"**{PRESET_ROLES[role_choices[0]]['name']}**\n\n{PRESET_ROLES[role_choices[0]]['description']}"
            )
            
            # 自定义角色区域
            with gr.Group(visible=False) as custom_role_group:
                gr.Markdown("### ✨ 自定义角色")
                custom_name = gr.Textbox(label="角色名称", placeholder="例如：未来科学家")
                custom_prompt = gr.Textbox(
                    label="系统提示词",
                    placeholder="描述角色的性格、说话方式、专长等...",
                    lines=5
                )
                custom_greeting = gr.Textbox(
                    label="开场白（可选）",
                    placeholder="角色的第一句话..."
                )
            
            set_role_btn = gr.Button("🎭 开始角色扮演", variant="primary", size="lg")
            role_status = gr.Markdown("")
            
            gr.Markdown("""
            ### 💡 提示
            
            - 不同角色有不同的性格和说话风格
            - 尝试与角色互动，探索它们的特点
            - 自定义角色可以创造无限可能
            
            ### ⚙️ 当前配置
            """)
            
            if llm:
                gr.Markdown("✅ AI模型已就绪")
            else:
                gr.Markdown("❌ 请配置API Key")
        
        with gr.Column(scale=2):
            gr.Markdown("### 💬 对话区")
            
            chatbot = gr.Chatbot(
                height=500,
                label="与AI角色对话",
                avatar_images=(None, "🎭")
            )
            
            with gr.Row():
                msg = gr.Textbox(
                    label="输入消息",
                    placeholder="在这里输入你想说的话...",
                    scale=4
                )
                send_btn = gr.Button("发送", variant="primary", scale=1)
            
            with gr.Row():
                reset_btn = gr.Button("🔄 重置对话")
                clear_btn = gr.Button("🗑️ 清空")
    
    # 更新角色信息显示
    def update_role_info(role_name):
        if role_name == "🎭 自定义角色":
            return "", gr.update(visible=True)
        else:
            role = PRESET_ROLES[role_name]
            info = f"**{role['name']}**\n\n{role['description']}"
            return info, gr.update(visible=False)
    
    # 事件绑定
    role_selector.change(
        update_role_info,
        role_selector,
        [role_info, custom_role_group]
    )
    
    set_role_btn.click(
        set_role,
        [role_selector, custom_name, custom_prompt, custom_greeting],
        [role_status, msg]
    )
    
    # 聊天功能
    def user(user_message, history):
        return "", history + [[user_message, None]]
    
    def bot(history):
        user_message = history[-1][0]
        bot_message = chat_with_role(user_message, history)
        history[-1][1] = bot_message
        return history
    
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    send_btn.click(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    reset_btn.click(reset_conversation, None, chatbot)
    clear_btn.click(lambda: None, None, chatbot, queue=False)


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🎭 AI角色扮演游戏")
    print("=" * 60)
    
    if llm:
        print("✅ AI模型已就绪")
    else:
        print("❌ 未配置 API Key")
        print("请在.env文件中配置 API Key")
    
    print("\n" + "=" * 60)
    print("🚀 启动中...")
    print("=" * 60 + "\n")
    
    try:
        demo.queue().launch(
            server_name="127.0.0.1",
            server_port=7866,
            share=False
        )
    except Exception as e:
        print(f"\n❌ 启动失败: {e}")
        print("尝试使用命令行版本: python role_play_cli.py")
