// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package logic

import (
	"context"

	"ai-role-play-app-go-server/internal/svc"
	"ai-role-play-app-go-server/internal/types"

	"github.com/zeromicro/go-zero/core/logx"
)

type GetRolesLogic struct {
	logx.Logger
	ctx    context.Context
	svcCtx *svc.ServiceContext
}

func NewGetRolesLogic(ctx context.Context, svcCtx *svc.ServiceContext) *GetRolesLogic {
	return &GetRolesLogic{
		Logger: logx.WithContext(ctx),
		ctx:    ctx,
		svcCtx: svcCtx,
	}
}

func (l *GetRolesLogic) GetRoles(req *types.GetRolesRequest) (resp *types.GetRolesResponse, err error) {
	// 示例数据，实际应该从数据库获取
	roles := []types.Role{
		{
			Id:          1,
			Name:        "历史学家",
			Description: "一位博学的历史学家，对世界历史了如指掌",
			Personality: "博学、严谨、善于讲述历史故事",
		},
		{
			Id:          2,
			Name:        "科幻作家",
			Description: "一位富有想象力的科幻作家，擅长创作未来世界的故事",
			Personality: "创新、乐观、充满想象力",
		},
		{
			Id:          3,
			Name:        "心理咨询师",
			Description: "一位经验丰富的心理咨询师，善于倾听和提供建议",
			Personality: "温和、耐心、善解人意",
		},
	}

	return &types.GetRolesResponse{
		Roles: roles,
	}, nil
}
