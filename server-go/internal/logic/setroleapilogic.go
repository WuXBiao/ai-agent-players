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

type SetRoleApiLogic struct {
	logx.Logger
	ctx    context.Context
	svcCtx *svc.ServiceContext
}

func NewSetRoleApiLogic(ctx context.Context, svcCtx *svc.ServiceContext) *SetRoleApiLogic {
	return &SetRoleApiLogic{
		Logger: logx.WithContext(ctx),
		ctx:    ctx,
		svcCtx: svcCtx,
	}
}

func (l *SetRoleApiLogic) SetRoleApi(req *types.SetRoleApiRequest) (resp *types.SetRoleApiResponse, err error) {
	// 检查gRPC客户端是否可用
	if l.svcCtx.GrpcClient == nil {
		logx.Info("gRPC client is not available, returning mock data")
		// 返回模拟数据
		return &types.SetRoleApiResponse{
			Success:  true,
			Message:  "角色设置成功",
			Greeting: "你好，我是 " + req.RoleName + "，很高兴与你交流！",
		}, nil
	}

	// 调用Python gRPC服务设置角色
	grpcReq := &grpc.SetRoleRequest{
		RoleName: req.RoleName,
	}

	grpcResp, err := l.svcCtx.GrpcClient.SetRole(l.ctx, grpcReq)
	if err != nil {
		logx.Errorf("Failed to call Python gRPC service: %v", err)
		return nil, err
	}

	if !grpcResp.Success {
		logx.Errorf("Python gRPC service returned error: %s", grpcResp.Message)
		return nil, err
	}

	return &types.SetRoleApiResponse{
		Success:  grpcResp.Success,
		Message:  grpcResp.Message,
		Greeting: grpcResp.Greeting,
	}, nil
}
