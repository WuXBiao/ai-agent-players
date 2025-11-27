// Code scaffolded by goctl. Safe to edit.
// goctl 1.9.2

package handler

import (
	"net/http"

	"ai-role-play-app-go-server/internal/logic"
	"ai-role-play-app-go-server/internal/svc"
	"ai-role-play-app-go-server/internal/types"
	"github.com/zeromicro/go-zero/rest/httpx"
)

func GetRoleHandler(svcCtx *svc.ServiceContext) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var req types.GetRoleRequest
		if err := httpx.Parse(r, &req); err != nil {
			httpx.ErrorCtx(r.Context(), w, err)
			return
		}

		l := logic.NewGetRoleLogic(r.Context(), svcCtx)
		resp, err := l.GetRole(&req)
		if err != nil {
			httpx.ErrorCtx(r.Context(), w, err)
		} else {
			httpx.OkJsonCtx(r.Context(), w, resp)
		}
	}
}
