// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package logic

import (
	"context"
	"strconv"
	"time"

	"serve-go/internal/grpc"
	"serve-go/internal/svc"
	"serve-go/internal/types"

	"github.com/zeromicro/go-zero/core/logx"
)

type SendMessageLogic struct {
	logx.Logger
	ctx    context.Context
	svcCtx *svc.ServiceContext
}

func NewSendMessageLogic(ctx context.Context, svcCtx *svc.ServiceContext) *SendMessageLogic {
	return &SendMessageLogic{
		Logger: logx.WithContext(ctx),
		ctx:    ctx,
		svcCtx: svcCtx,
	}
}

func (l *SendMessageLogic) SendMessage(req *types.SendMessageRequest) (resp *types.SendMessageResponse, err error) {
	// 将字符串 RoleId 转换为 int
	roleId, err := strconv.Atoi(req.RoleId)
	if err != nil {
		logx.Errorf("Invalid role_id: %v", err)
		return nil, err
	}

	// 调用Python gRPC服务获取回复
	responseContent, err := l.callPythonGrpcService(roleId, req.Content)
	if err != nil {
		return nil, err
	}

	message := types.Message{
		Id:        int(time.Now().Unix()),
		RoleId:    roleId,
		Content:   responseContent,
		Timestamp: time.Now().Format("2006-01-02 15:04:05"),
	}

	return &types.SendMessageResponse{
		Message: message,
	}, nil
}

func (l *SendMessageLogic) callPythonGrpcService(roleId int, userMessage string) (string, error) {
	// 检查gRPC客户端是否可用
	if l.svcCtx.GrpcClient == nil {
		logx.Info("gRPC client is not available, returning mock data")
		// 返回模拟数据
		roleNames := map[int]string{
			1: "🧙‍♂️ 智慧导师",
			2: "🚀 科幻作家",
			3: "❤️ 心理咨询师",
		}

		roleName := roleNames[roleId]
		if roleName == "" {
			roleName = "🧙‍♂️ 智慧导师" // 默认角色
		}

		// 模拟AI回复
		responses := map[string]string{
			"🧙‍♂️ 智慧导师": "作为一位智慧导师，我对你的问题很感兴趣。在历史的长河中，类似的思考曾启发了许多伟大的思想家。我认为...",
			"🚀 科幻作家":    "哇，这是个很有趣的想法！在我的想象中，未来的世界可能会是这样的...",
			"❤️ 心理咨询师":  "我理解你的感受。从心理学的角度来看，这种情况可能反映了...",
		}

		response, exists := responses[roleName]
		if !exists {
			response = "你好，我是AI助手，很高兴与你交流！"
		}

		return response, nil
	}

	// 调用Python gRPC服务进行对话（假设角色已通过 /roles/set 端点设置）
	chatReq := &grpc.ChatRequest{
		Message: userMessage,
	}

	chatResp, err := l.svcCtx.GrpcClient.ChatWithRole(l.ctx, chatReq)
	if err != nil {
		logx.Errorf("Failed to call Python gRPC service: %v", err)
		return "", err
	}

	if !chatResp.Success {
		logx.Errorf("Python gRPC service returned error: %s", chatResp.Error)
		return "", err
	}

	return chatResp.Response, nil
}
