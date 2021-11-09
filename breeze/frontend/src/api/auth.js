import  { requestLogin, requestLogout, requestCheck } from '@/utils/request.js';
import SERVER from './drf.js';

const authApi = {

  login: (code) => {
    console.log('로그인 axios 보내기 1초 전')
    return requestLogin(SERVER.ROUTES.auth + `/login/?code=${code}`)
  },

  logout: () => {
    console.log('로그아웃 axios 보내기 1초 전')
    return requestLogout(SERVER.ROUTES.auth + '/logout/')
  },

  check: () => {
    console.log('라우터 이동 시 토큰 만료 여부 체크')
    return requestCheck(SERVER.ROUTES.auth + '/check/')
  }

};

export default authApi;