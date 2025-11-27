// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package logic

import (
	"context"

	"serve-go/internal/grpc"
	"serve-go/internal/svc"
	"serve-go/internal/types"

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
	// 检查gRPC客户端是否可用
	if l.svcCtx.GrpcClient == nil {
		logx.Info("gRPC client is not available, returning mock data")
		// 返回模拟数据
		roles := []types.Role{
			{
				Id:          1,
				Name:        "🧙‍♂️ 智慧导师",
				Description: "一位博学的导师，能够回答各种问题并提供深刻见解",
				Personality: "博学、智慧、耐心",
			},
			{
				Id:          2,
				Name:        "🚀 科幻作家",
				Description: "富有想象力的科幻作家，擅长创作未来世界的故事",
				Personality: "创新、乐观、充满想象力",
			},
			{
				Id:          3,
				Name:        "❤️ 心理咨询师",
				Description: "经验丰富的心理咨询师，善于倾听和提供建议",
				Personality: "温和、耐心、善解人意",
			},
		}

		return &types.GetRolesResponse{
			Roles: roles,
		}, nil
	}

	// 调用Python gRPC服务获取角色列表
	grpcResp, err := l.svcCtx.GrpcClient.GetPresetRoles(l.ctx, &grpc.GetPresetRolesRequest{})
	if err != nil {
		logx.Errorf("Failed to call Python gRPC service: %v", err)
		return nil, err
	}

	// 转换角色数据
	var roles []types.Role
	for i, role := range grpcResp.Roles {
		roles = append(roles, types.Role{
			Id:          i + 1,
			Name:        role.GetName(),
			Description: role.GetDescription(),
			Personality: "", // Python服务没有提供这个字段
		})
	}

	return &types.GetRolesResponse{
		Roles: roles,
	}, nil
}
