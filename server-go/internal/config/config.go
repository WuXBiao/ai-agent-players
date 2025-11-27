// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package config

import "github.com/zeromicro/go-zero/rest"

type Config struct {
	rest.RestConf
	DataSource  DataSourceConf
	GrpcService GrpcServiceConf
}

type DataSourceConf struct {
	Host     string
	Port     int
	Database string
	Username string
	Password string
}

type GrpcServiceConf struct {
	Address string
	Timeout int64
}
