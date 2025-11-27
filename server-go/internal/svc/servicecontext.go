// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package svc

import (
	"serve-go/internal/config"
	"serve-go/internal/grpc"
)

type ServiceContext struct {
	Config     config.Config
	GrpcClient *grpc.Client
}

func NewServiceContext(c config.Config) *ServiceContext {
	// Create gRPC client
	grpcClient, err := grpc.NewClient(c.GrpcService)
	if err != nil {
		panic(err)
	}

	return &ServiceContext{
		Config:     c,
		GrpcClient: grpcClient,
	}
}
