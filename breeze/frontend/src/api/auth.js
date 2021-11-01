import  { requestLogin, requestLogout, requestCheck } from '@/utils/request.js';
// import SERVER from './drf.js';

const authApi = {

  login: (data) => {
    console.log('로그인 axios 보내기 1초 전')
    return requestLogin(`/auth/login/?code=${data}`)
  },

  logout: (id) => {
    console.log('로그아웃 axios 보내기 1초 전')
    return requestLogout(`/auth/logout/?id=${id}`)
  },

  check: (id) => {
    console.log('라우터 이동 시 토큰 만료 여부 체크')
    return requestCheck(`/auth/check/?id=${id}`)
  }

};

export default authApi;