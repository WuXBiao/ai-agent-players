// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package config

import "github.com/zeromicro/go-zero/rest"

type Config struct {
	rest.RestConf
	AiService  AiServiceConf
	DataSource DataSourceConf
}

type AiServiceConf struct {
	ApiKey  string
	Model   string
	Timeout int64
}

type DataSourceConf struct {
	Host     string
	Port     int
	Database string
	Username string
	Password string
}
