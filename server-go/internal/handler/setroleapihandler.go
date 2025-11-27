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

func SetRoleApiHandler(svcCtx *svc.ServiceContext) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var req types.SetRoleApiRequest
		if err := httpx.Parse(r, &req); err != nil {
			logx.Errorf("Failed to parse request: %v", err)
			httpx.ErrorCtx(r.Context(), w, err)
			return
		}

		l := logic.NewSetRoleApiLogic(r.Context(), svcCtx)
		resp, err := l.SetRoleApi(&req)
		if err != nil {
			logx.Errorf("Failed to set role: %v", err)
			httpx.ErrorCtx(r.Context(), w, err)
		} else {
			logx.Infof("Successfully set role: %v", resp)
			httpx.OkJsonCtx(r.Context(), w, resp)
		}
	}
}
