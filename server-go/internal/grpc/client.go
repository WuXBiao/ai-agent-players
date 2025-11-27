package grpc

import (
	"context"
	"time"

	"serve-go/internal/config"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

// Client wraps the gRPC client for RolePlayService
type Client struct {
	conn   *grpc.ClientConn
	client RolePlayServiceClient
	config config.GrpcServiceConf
}

// NewClient creates a new gRPC client
func NewClient(config config.GrpcServiceConf) (*Client, error) {
	// Create gRPC connection
	ctx, cancel := context.WithTimeout(context.Background(), time.Duration(config.Timeout)*time.Millisecond)
	defer cancel()

	conn, err := grpc.DialContext(ctx, config.Address, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		return nil, err
	}

	client := NewRolePlayServiceClient(conn)

	return &Client{
		conn:   conn,
		client: client,
		config: config,
	}, nil
}

// Close closes the gRPC connection
func (c *Client) Close() error {
	return c.conn.Close()
}

// SetRole calls the SetRole RPC method on the Python gRPC service
func (c *Client) SetRole(ctx context.Context, req *SetRoleRequest) (*SetRoleResponse, error) {
	// Set timeout for the request
	timeoutCtx, cancel := context.WithTimeout(ctx, time.Duration(c.config.Timeout)*time.Millisecond)
	defer cancel()

	return c.client.SetRole(timeoutCtx, req)
}

// ChatWithRole calls the ChatWithRole RPC method on the Python gRPC service
func (c *Client) ChatWithRole(ctx context.Context, req *ChatRequest) (*ChatResponse, error) {
	// Set timeout for the request
	timeoutCtx, cancel := context.WithTimeout(ctx, time.Duration(c.config.Timeout)*time.Millisecond)
	defer cancel()

	return c.client.ChatWithRole(timeoutCtx, req)
}

// GetPresetRoles calls the GetPresetRoles RPC method on the Python gRPC service
func (c *Client) GetPresetRoles(ctx context.Context, req *GetPresetRolesRequest) (*GetPresetRolesResponse, error) {
	// Set timeout for the request
	timeoutCtx, cancel := context.WithTimeout(ctx, time.Duration(c.config.Timeout)*time.Millisecond)
	defer cancel()

	return c.client.GetPresetRoles(timeoutCtx, req)
}
