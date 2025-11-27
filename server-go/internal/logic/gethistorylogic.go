// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package logic

import (
	"context"
	"time"

	"serve-go/internal/svc"
	"serve-go/internal/types"

	"github.com/zeromicro/go-zero/core/logx"
)

type GetHistoryLogic struct {
	logx.Logger
	ctx    context.Context
	svcCtx *svc.ServiceContext
}

func NewGetHistoryLogic(ctx context.Context, svcCtx *svc.ServiceContext) *GetHistoryLogic {
	return &GetHistoryLogic{
		Logger: logx.WithContext(ctx),
		ctx:    ctx,
		svcCtx: svcCtx,
	}
}

func (l *GetHistoryLogic) GetHistory(req *types.GetHistoryRequest) (resp *types.GetHistoryResponse, err error) {
	// TODO: 实现从Python gRPC服务或数据库获取真实的历史记录
	// 目前返回示例数据
	messages := []types.Message{
		{
			Id:        1,
			RoleId:    req.RoleId,
			Content:   "您好，我是历史学家，有什么我可以帮助您的吗？",
			Timestamp: time.Now().Add(-30 * time.Minute).Format("2006-01-02 15:04:05"),
		},
		{
			Id:        2,
			RoleId:    req.RoleId,
			Content:   "用户：我想了解中国古代的丝绸之路。",
			Timestamp: time.Now().Add(-25 * time.Minute).Format("2006-01-02 15:04:05"),
		},
		{
			Id:        3,
			RoleId:    req.RoleId,
			Content:   "作为历史学家，我对您提到的内容很感兴趣。丝绸之路是古代中国与西方的重要贸易通道...",
			Timestamp: time.Now().Add(-20 * time.Minute).Format("2006-01-02 15:04:05"),
		},
	}

	return &types.GetHistoryResponse{
		Messages: messages,
	}, nil
}
