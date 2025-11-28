"""
AI角色扮演 - 命令行版本
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 预设角色
ROLES = {
    "1": {
        "name": "🧙‍♂️ 智慧导师",
        "prompt": "你是一位智慧的导师，善于用简单的例子解释复杂问题。语气温和且富有启发性。",
        "greeting": "欢迎！我是你的智慧导师。有什么问题想要探讨吗？"
    },
    "2": {
        "name": "🎭 莎士比亚", 
        "prompt": "你是莎士比亚，用富有诗意的语言表达，对人性有深刻洞察。",
        "greeting": "你好啊，亲爱的朋友！莎士比亚在此，愿为汝分享诗歌与智慧。"
    },
    "3": {
        "name": "🤖 未来AI",
        "prompt": "你是来自2050年的AI，了解未来科技发展，用未来主义视角看问题。",
        "greeting": "你好，2024年的朋友！我是来自2050年的ARIA。很高兴与你交流！"
    },
    "4": {
        "name": "🧑‍🍳 米其林大厨",
        "prompt": "你是米其林三星大厨，对美食充满激情，善于分享烹饪技巧。",
        "greeting": "Bonjour! 我是Chef Antoine！让我们探索美食的奇妙世界吧！"
    },
    "5": {
        "name": "🐱 傲娇猫娘",
        "prompt": "你是可爱的傲娇猫娘小喵，说话用'喵~'作语气词，外冷内热。",
        "greeting": "哼~居然让本喵等这么久！不、不是在等你哦喵~"
    },
    "6": {
        "name": "🕵️ 福尔摩斯",
        "prompt": "你是夏洛克·福尔摩斯，逻辑推理能力超群，观察力敏锐。",
        "greeting": "Good day! 我是福尔摩斯。有什么谜团需要我解开吗？"
    },
    "7": {
        "name": "💪 健身教练",
        "prompt": "你是充满活力的健身教练Max，专业且富有激励性。",
        "greeting": "嘿！我是Max，你的私人教练！准备好挑战自己了吗？Let's go!"
    },
    "8": {
        "name": "🎨 艺术评论家",
        "prompt": "你是知名艺术评论家，对各种艺术形式有深刻理解，用优雅语言表达。",
        "greeting": "您好！很高兴与您探讨艺术。让我们欣赏这美妙的世界吧。"
    }
}

def init_llm():
    """初始化大模型"""
    siliconflow_key = os.getenv("SILICONFLOW_API_KEY")
    zhipu_key = os.getenv("ZHIPU_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if siliconflow_key:
        print("使用硅基流动模型...")
        return ChatOpenAI(
            model="Qwen/Qwen2.5-7B-Instruct",
            temperature=0.9,
            api_key=siliconflow_key,  # type: ignore
            base_url="https://api.siliconflow.cn/v1"
        )
    elif zhipu_key:
        print("使用智谱AI模型...")
        return ChatOpenAI(
            model="glm-4-flash",
            temperature=0.9,
            api_key=zhipu_key,  # type: ignore
            base_url="https://open.bigmodel.cn/api/paas/v4/"
        )
    elif openai_key:
        print("使用OpenAI模型...")
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.9,
            api_key=openai_key  # type: ignore
        )
    else:
        return None

def main():
    print("\n" + "="*60)
    print("🎭 AI角色扮演游戏 (命令行版)")
    print("="*60)
    
    llm = init_llm()
    if not llm:
        print("\n❌ 未配置API Key!")
        print("请在.env文件中配置以下任一Key:")
        print("  - SILICONFLOW_API_KEY")
        print("  - ZHIPU_API_KEY")
        print("  - OPENAI_API_KEY")
        return
    
    print("\n✅ AI模型已就绪\n")
    
    # 选择角色
    print("请选择一个角色:\n")
    for key, role in ROLES.items():
        print(f"  {key}. {role['name']}")
    
    choice = input("\n输入编号 (1-8): ").strip()
    
    if choice not in ROLES:
        print("无效选择！")
        return
    
    role = ROLES[choice]
    print(f"\n{'='*60}")
    print(f"已选择角色: {role['name']}")
    print(f"{'='*60}")
    print(f"\n{role['greeting']}\n")
    
    # 对话循环
    history = []
    
    while True:
        user_input = input("\n你: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit', 'q', '退出', '结束']:
            print(f"\n再见！很高兴与你交流！\n")
            break
        
        if user_input.lower() in ['reset', '重置']:
            history = []
            print(f"\n对话已重置。\n{role['greeting']}\n")
            continue
        
        try:
            # 构建消息
            messages = [SystemMessage(content=role['prompt'])]
            for h in history:
                messages.append(HumanMessage(content=h['user']))
                messages.append(AIMessage(content=h['ai']))
            messages.append(HumanMessage(content=user_input))
            
            # 获取响应
            print(f"\n{role['name']}: ", end="", flush=True)
            response = llm.invoke(messages)
            ai_response = response.content
            print(ai_response)
            
            # 保存历史
            history.append({
                'user': user_input,
                'ai': ai_response
            })
            
        except Exception as e:
            print(f"\n❌ 错误: {str(e)}")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
