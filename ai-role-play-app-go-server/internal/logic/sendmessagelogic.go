// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package logic

import (
	"context"
	"time"

	"ai-role-play-app-go-server/internal/svc"
	"ai-role-play-app-go-server/internal/types"

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
	// 模拟调用AI服务获取回复
	// 实际应该调用AI服务API
	responseContent := l.generateAIResponse(req.RoleId, req.Content)

	message := types.Message{
		Id:        int(time.Now().Unix()),
		RoleId:    req.RoleId,
		Content:   responseContent,
		Timestamp: time.Now().Format("2006-01-02 15:04:05"),
	}

	return &types.SendMessageResponse{
		Message: message,
	}, nil
}

func (l *SendMessageLogic) generateAIResponse(roleId int, userMessage string) string {
	// 根据角色ID生成不同的回复
	roleResponses := map[int]string{
		1: "作为历史学家，我对您提到的内容很感兴趣。在历史上，类似的事件曾发生在...",
		2: "作为一名科幻作家，我认为您的想法很有创意！在未来的世界里，这可能会演变成...",
		3: "我理解您的感受。作为心理咨询师，我想建议您可以尝试...",
	}

	if response, exists := roleResponses[roleId]; exists {
		return response
	}

	return "您好，我是AI助手，很高兴与您交流！"
}
