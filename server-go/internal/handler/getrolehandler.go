// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package handler

import (
	"net/http"

	"serve-go/internal/logic"
	"serve-go/internal/svc"
	"serve-go/internal/types"

	"github.com/zeromicro/go-zero/core/logx"
	"github.com/zeromicro/go-zero/rest/httpx"
)

func GetRoleHandler(svcCtx *svc.ServiceContext) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		logx.Infof("Received request: %s %s", r.Method, r.URL.Path)
		logx.Infof("Request headers: %v", r.Header)

		var req types.GetRoleRequest
		if err := httpx.Parse(r, &req); err != nil {
			logx.Errorf("Failed to parse request: %v", err)
			httpx.ErrorCtx(r.Context(), w, err)
			return
		}

		l := logic.NewGetRoleLogic(r.Context(), svcCtx)
		resp, err := l.GetRole(&req)
		if err != nil {
			logx.Errorf("Failed to get role: %v", err)
			httpx.ErrorCtx(r.Context(), w, err)
		} else {
			logx.Infof("Successfully got role: %v", resp)
			httpx.OkJsonCtx(r.Context(), w, resp)
		}
	}
}
