"""
AI角色扮演 Android APP
使用 Kivy 框架开发
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.factory import Factory
import sys
import os

# 添加父目录到路径，以便导入现有模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 注册中文字体
LabelBase.register(
    name='SimHei',
    fn_regular='C:/Windows/Fonts/simhei.ttf'  # 黑体
)
LabelBase.register(
    name='SimSun',
    fn_regular='C:/Windows/Fonts/simsun.ttc'  # 宋体
)

# 为Spinner选项设置中文字体
from kivy.uix.spinner import SpinnerOption
SpinnerOption.font_name = 'SimHei'
SpinnerOption.font_size = 16

# 预设角色配置（移除emoji，使用文字）
ROLES = {
    "智慧导师": {
        "name": "智慧导师",
        "icon": "[导师]",
        "prompt": "你是一位智慧的导师，善于用简单的例子解释复杂问题。语气温和且富有启发性。",
        "greeting": "欢迎！我是你的智慧导师。有什么问题想要探讨吗？"
    },
    "莎士比亚": {
        "name": "莎士比亚",
        "icon": "[诗人]",
        "prompt": "你是莎士比亚，用富有诗意的语言表达，对人性有深刻洞察。",
        "greeting": "你好啊，亲爱的朋友！莎士比亚在此，愿为汝分享诗歌与智慧。"
    },
    "未来AI": {
        "name": "未来AI",
        "icon": "[AI]",
        "prompt": "你是来自2050年的AI，了解未来科技发展，用未来主义视角看问题。",
        "greeting": "你好，2024年的朋友！我是来自2050年的ARIA。很高兴与你交流！"
    },
    "米其林大厨": {
        "name": "米其林大厨",
        "icon": "[大厨]",
        "prompt": "你是米其林三星大厨，对美食充满激情，善于分享烹饪技巧。",
        "greeting": "Bonjour! 我是Chef Antoine！让我们探索美食的奇妙世界吧！"
    },
    "傲娇猫娘": {
        "name": "傲娇猫娘",
        "icon": "[猫娘]",
        "prompt": "你是可爱的傲娇猫娘小喵，说话用'喵~'作语气词，外冷内热。",
        "greeting": "哼~居然让本喵等这么久！不、不是在等你哦喵~"
    },
    "福尔摩斯": {
        "name": "福尔摩斯",
        "icon": "[侦探]",
        "prompt": "你是夏洛克·福尔摩斯，逻辑推理能力超群，观察力敏锐。",
        "greeting": "Good day! 我是福尔摩斯。有什么谜团需要我解开吗？"
    },
    "健身教练": {
        "name": "健身教练",
        "icon": "[教练]",
        "prompt": "你是充满活力的健身教练Max，专业且富有激励性。",
        "greeting": "嘿！我是Max，你的私人教练！准备好挑战自己了吗？Let's go!"
    },
    "艺术评论家": {
        "name": "艺术评论家",
        "icon": "[艺术]",
        "prompt": "你是知名艺术评论家，对各种艺术形式有深刻理解，用优雅语言表达。",
        "greeting": "您好！很高兴与您探讨艺术。让我们欣赏这美妙的世界吧。"
    }
}


class ChatMessage(Label):
    """聊天消息组件"""
    pass


class RolePlayApp(App):
    """AI角色扮演 APP"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.llm = None
        self.current_role = None
        self.conversation_history = []
        
    def build(self):
        """构建 UI - 现代化设计"""
        # 设置窗口背景色为渐变蓝
        Window.clearcolor = (0.94, 0.96, 0.98, 1)
        Window.size = (400, 700)  # 手机屏幕比例
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=12)
        
        # === 顶部栏 ===
        top_bar = BoxLayout(
            size_hint_y=None,
            height=70,
            padding=[15, 10],
            spacing=10
        )
        
        # 标题
        title = Label(
            text='AI 角色扮演',
            size_hint_x=0.7,
            font_size='28sp',
            font_name='SimHei',
            bold=True,
            color=(0.15, 0.25, 0.45, 1),
            halign='left',
            valign='middle'
        )
        title.bind(size=title.setter('text_size'))
        
        top_bar.add_widget(title)
        main_layout.add_widget(top_bar)
        
        # === 角色选择卡片 ===
        role_card = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=90,
            padding=15,
            spacing=8
        )
        
        role_label = Label(
            text='当前角色',
            size_hint_y=None,
            height=25,
            font_size='14sp',
            font_name='SimHei',
            color=(0.4, 0.4, 0.4, 1),
            halign='left'
        )
        role_label.bind(size=role_label.setter('text_size'))
        
        self.role_spinner = Spinner(
            text='点击选择角色',
            values=list(ROLES.keys()),
            size_hint_y=None,
            height=45,
            font_size='16sp',
            font_name='SimHei',
            background_color=(1, 1, 1, 1),
            color=(0.2, 0.2, 0.2, 1),
            background_normal='',
            background_down='',
            option_cls=Factory.SpinnerOption
        )
        self.role_spinner.bind(text=self.on_role_selected)
        
        role_card.add_widget(role_label)
        role_card.add_widget(self.role_spinner)
        main_layout.add_widget(role_card)
        
        # === 聊天区域 ===
        scroll = ScrollView(
            size_hint=(1, 1),
            do_scroll_x=False,
            bar_width=8,
            bar_color=(0.7, 0.7, 0.7, 0.5),
            bar_inactive_color=(0.9, 0.9, 0.9, 0.3)
        )
        self.chat_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=12,
            padding=[10, 15]
        )
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        scroll.add_widget(self.chat_layout)
        main_layout.add_widget(scroll)
        
        # === 输入区域 ===
        input_card = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=120,
            padding=[10, 8],
            spacing=8
        )
        
        input_row = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        self.text_input = TextInput(
            hint_text='输入消息...',
            multiline=False,
            size_hint_x=0.78,
            font_size='15sp',
            font_name='SimHei',
            padding=[15, 15],
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            cursor_color=(0.3, 0.6, 1, 1),
            background_normal='',
            background_active=''
        )
        
        send_btn = Button(
            text='发送',
            size_hint_x=0.22,
            font_size='15sp',
            font_name='SimHei',
            bold=True,
            background_color=(0.25, 0.55, 0.95, 1),
            color=(1, 1, 1, 1),
            background_normal='',
            background_down=''
        )
        send_btn.bind(on_press=self.send_message)
        
        input_row.add_widget(self.text_input)
        input_row.add_widget(send_btn)
        
        # 底部按钮行
        btn_row = BoxLayout(size_hint_y=None, height=45, spacing=10)
        
        reset_btn = Button(
            text='重置',
            font_size='14sp',
            font_name='SimHei',
            background_color=(0.95, 0.65, 0.25, 1),
            color=(1, 1, 1, 1),
            background_normal='',
            background_down=''
        )
        reset_btn.bind(on_press=self.reset_conversation)
        
        clear_btn = Button(
            text='清空',
            font_size='14sp',
            font_name='SimHei',
            background_color=(0.9, 0.4, 0.4, 1),
            color=(1, 1, 1, 1),
            background_normal='',
            background_down=''
        )
        clear_btn.bind(on_press=self.clear_chat)
        
        btn_row.add_widget(reset_btn)
        btn_row.add_widget(clear_btn)
        
        input_card.add_widget(input_row)
        input_card.add_widget(btn_row)
        main_layout.add_widget(input_card)
        
        # 初始化 LLM
        self.init_llm()
        
        return main_layout
    
    def init_llm(self):
        """初始化大模型 - 增强版错误处理和连接验证"""
        zhipu_key = os.getenv("ZHIPU_API_KEY")
        siliconflow_key = os.getenv("SILICONFLOW_API_KEY")
        openai_key = os.getenv("OPENAI_API_KEY")
        
        # 清理可能的引号和空白
        if zhipu_key:
            zhipu_key = zhipu_key.strip("'\" ")
        if siliconflow_key:
            siliconflow_key = siliconflow_key.strip("'\" ")
        if openai_key:
            openai_key = openai_key.strip("'\" ")
        
        try:
            if zhipu_key:
                self.llm = ChatOpenAI(
                    model="glm-4-flash",
                    temperature=0.9,
                    api_key=zhipu_key,  # type: ignore
                    base_url="https://open.bigmodel.cn/api/paas/v4/"
                )
                # 验证连接
                if self.test_connection(self.llm):
                    self.add_system_message("✅ 智谱AI模型已就绪")
                else:
                    self.add_system_message("❌ 智谱AI连接失败，尝试其他模型")
                    self.llm = None
            elif siliconflow_key:
                self.llm = ChatOpenAI(
                    model="Qwen/Qwen2.5-7B-Instruct",
                    temperature=0.9,
                    api_key=siliconflow_key,  # type: ignore
                    base_url="https://api.siliconflow.cn/v1"
                )
                # 验证连接
                if self.test_connection(self.llm):
                    self.add_system_message("✅ 硅基流动模型已就绪")
                else:
                    self.add_system_message("❌ 硅基流动连接失败，尝试其他模型")
                    self.llm = None
            elif openai_key:
                self.llm = ChatOpenAI(
                    model="gpt-3.5-turbo",
                    temperature=0.9,
                    api_key=openai_key  # type: ignore
                )
                # 验证连接
                if self.test_connection(self.llm):
                    self.add_system_message("✅ OpenAI模型已就绪")
                else:
                    self.add_system_message("❌ OpenAI连接失败")
                    self.llm = None
            else:
                self.add_system_message("❌ 未配置API Key\n请在.env文件中配置")
        except Exception as e:
            self.add_system_message(f"❌ 模型初始化失败: {str(e)}")
            self.llm = None
    
    def test_connection(self, llm):
        """测试LLM连接"""
        try:
            # 发送一个简单的测试请求，使用正确的消息格式
            response = llm.invoke([
                SystemMessage(content="你是一个AI助手"),
                HumanMessage(content="你好")
            ])
            return True
        except Exception as e:
            print(f"连接测试失败: {e}")
            return False
    
    def add_system_message(self, text):
        """添加系统消息 - 现代化样式"""
        msg = Label(
            text=text,
            size_hint_y=None,
            height=35,
            font_size='13sp',
            font_name='SimHei',
            color=(0.5, 0.5, 0.5, 1),
            halign='center',
            italic=True
        )
        msg.bind(size=msg.setter('text_size'))
        
        # 使用Clock.schedule_once确保在布局完成后再添加消息
        from kivy.clock import Clock
        def add_widget_and_scroll(dt):
            self.chat_layout.add_widget(msg)
            
            # 系统消息也需要滚动到底部
            def scroll_to_bottom(dt):
                scroll_view = self.chat_layout.parent
                if scroll_view:
                    from kivy.animation import Animation
                    Animation(scroll_y=0, duration=0.3).start(scroll_view)
            Clock.schedule_once(scroll_to_bottom, 0.1)
            
        Clock.schedule_once(add_widget_and_scroll, 0)
    
    def add_message(self, text, is_user=True):
        """添加聊天消息 - 聊天气泡样式"""
        # 获取屏幕宽度
        from kivy.core.window import Window
        screen_width = Window.width
        max_msg_width = screen_width * 0.7  # 消息最大宽度为屏幕的70%
        
        # 创建消息行容器
        row = BoxLayout(
            size_hint_y=None,
            height=70,  # 默认高度
            padding=[10, 5],
            spacing=10
        )
        
        # 消息内容
        msg = Label(
            text=text,
            size_hint=(None, None),
            width=max_msg_width * (0.8 if is_user else 0.8),
            font_size='15sp',
            font_name='SimHei',
            halign='left' if not is_user else 'right',
            valign='top',
            padding=[20, 15],
            text_size=(max_msg_width * (0.8 if is_user else 0.8) - 40, None)
        )
        
        # 设置颜色
        if is_user:
            msg.color = (1, 1, 1, 1)  # 白色文字
            # 用户消息 - 右对齐
            row.add_widget(Label(size_hint_x=0.15))  # 左侧空白
            
            # 绘制气泡背景
            with msg.canvas.before:
                from kivy.graphics import Color, RoundedRectangle
                Color(0.25, 0.55, 0.95, 1)  # 蓝色背景
                self.user_bubble = RoundedRectangle(size=msg.size, pos=msg.pos, radius=[20, 20, 5, 20])
            
            # 绑定位置和大小更新
            def update_user_bubble(*args):
                self.user_bubble.pos = msg.pos
                self.user_bubble.size = msg.size
            msg.bind(pos=update_user_bubble, size=update_user_bubble)
            
            row.add_widget(msg)
            row.add_widget(Label(size_hint_x=0.05))  # 右侧小空白
        else:
            msg.color = (0.2, 0.2, 0.2, 1)  # 深色文字
            # AI消息 - 左对齐
            row.add_widget(Label(size_hint_x=0.05))  # 左侧小空白
            
            # 绘制气泡背景
            with msg.canvas.before:
                from kivy.graphics import Color, RoundedRectangle
                Color(0.9, 0.9, 0.9, 1)  # 灰色背景
                self.ai_bubble = RoundedRectangle(size=msg.size, pos=msg.pos, radius=[20, 5, 20, 20])
            
            # 绑定位置和大小更新
            def update_ai_bubble(*args):
                self.ai_bubble.pos = msg.pos
                self.ai_bubble.size = msg.size
            msg.bind(pos=update_ai_bubble, size=update_ai_bubble)
            
            row.add_widget(msg)
            row.add_widget(Label(size_hint_x=0.15))  # 右侧空白
        
        # 动态调整尺寸 - 修复错位问题
        def update_message_size(*args):
            # 更新高度
            new_height = max(50, msg.texture_size[1] + 30)
            msg.height = new_height
            row.height = max(70, new_height + 20)
            
            # 滚动到底部
            from kivy.clock import Clock
            def scroll_to_bottom(dt):
                scroll_view = self.chat_layout.parent
                if scroll_view:
                    from kivy.animation import Animation
                    Animation(scroll_y=0, duration=0.3).start(scroll_view)
            Clock.schedule_once(scroll_to_bottom, 0.02)
        
        # 使用更可靠的方式绑定尺寸更新
        msg.fbind('texture_size', update_message_size)
        
        # 使用Clock.schedule_once确保在布局完成后再添加消息
        from kivy.clock import Clock
        def add_widget_and_update(dt):
            self.chat_layout.add_widget(row)
            
            # 立即触发尺寸更新
            update_message_size()
            
        Clock.schedule_once(add_widget_and_update, 0)
    
    def on_role_selected(self, spinner, text):
        """角色选择回调"""
        if text in ROLES:
            self.current_role = ROLES[text]
            self.conversation_history = []
            self.chat_layout.clear_widgets()
            
            # 显示角色切换消息
            icon = self.current_role.get('icon', '')
            self.add_system_message(f"已选择: {icon} {self.current_role['name']}")
            self.add_message(self.current_role['greeting'], is_user=False)
    
    def send_message(self, instance):
        """发送消息"""
        user_message = self.text_input.text.strip()
        
        if not user_message:
            return
        
        if not self.current_role:
            self.add_system_message("⚠️ 请先选择角色")
            return
        
        if not self.llm:
            self.add_system_message("❌ 未配置API Key")
            return
        
        # 清空输入框
        self.text_input.text = ''
        
        # 显示用户消息
        self.add_message(user_message, is_user=True)
        
        # 异步获取AI响应
        Clock.schedule_once(lambda dt: self.get_ai_response(user_message), 0.1)
    
    def get_ai_response(self, user_message):
        """获取AI响应"""
        try:
            # 构建消息 - 确保消息列表不为空且格式正确
            messages = [SystemMessage(content=self.current_role['prompt'])]
            
            # 添加历史对话（如果有的话）
            for h in self.conversation_history:
                messages.append(HumanMessage(content=h['user']))
                messages.append(AIMessage(content=h['ai']))
            
            # 添加当前用户消息
            messages.append(HumanMessage(content=user_message))
            
            # 确保至少有一个用户消息
            if len([m for m in messages if isinstance(m, HumanMessage)]) == 0:
                messages.append(HumanMessage(content="你好"))
            
            # 显示正在思考（现代化样式）
            thinking_msg = Label(
                text="AI 正在思考中...",
                size_hint_y=None,
                height=35,
                font_size='13sp',
                font_name='SimHei',
                color=(0.6, 0.6, 0.6, 1),
                italic=True
            )
            
            # 确保"正在思考"消息可见
            from kivy.clock import Clock
            def add_thinking_and_scroll(dt):
                self.chat_layout.add_widget(thinking_msg)
                
                def scroll_thinking_into_view(dt):
                    scroll_view = self.chat_layout.parent
                    if scroll_view:
                        from kivy.animation import Animation
                        Animation(scroll_y=0, duration=0.3).start(scroll_view)
                Clock.schedule_once(scroll_thinking_into_view, 0.05)
                
            Clock.schedule_once(add_thinking_and_scroll, 0)
            
            # 获取响应
            response = self.llm.invoke(messages)
            ai_response = response.content
            
            # 移除"正在思考"
            self.chat_layout.remove_widget(thinking_msg)
            
            # 显示AI响应
            self.add_message(ai_response, is_user=False)
            
            # 保存历史
            self.conversation_history.append({
                'user': user_message,
                'ai': ai_response
            })
            
        except Exception as e:
            # 确保在异常情况下也能正确移除"正在思考"消息
            def remove_thinking_msg(dt):
                try:
                    if 'thinking_msg' in locals():
                        self.chat_layout.remove_widget(thinking_msg)
                except:
                    pass
                self.add_system_message(f"❌ 错误: {str(e)}")
            from kivy.clock import Clock
            Clock.schedule_once(remove_thinking_msg, 0)
    
    def _update_user_bubble(self, instance):
        """更新用户气泡图形"""
        if hasattr(self, 'user_bubble'):
            self.user_bubble.pos = instance.pos
            self.user_bubble.size = instance.size
    
    def _update_ai_bubble(self, instance):
        """更新AI气泡图形"""
        if hasattr(self, 'ai_bubble'):
            self.ai_bubble.pos = instance.pos
            self.ai_bubble.size = instance.size
    
    def clear_chat(self, instance):
        """清空聊天"""
        self.chat_layout.clear_widgets()
        self.conversation_history = []
    
    def reset_conversation(self, instance):
        """重置对话"""
        if self.current_role:
            self.conversation_history = []
            self.chat_layout.clear_widgets()
            
            # 显示角色切换消息
            icon = self.current_role.get('icon', '')
            self.add_system_message(f"已选择: {icon} {self.current_role['name']}")
            self.add_message(self.current_role['greeting'], is_user=False)


if __name__ == '__main__':
    RolePlayApp().run()