import  { requestLogin, requestPost } from '@/utils/request.js';
// import SERVER from './drf.js';

const authApi = {

  login: (data) => {
    console.log('로그인 axios 보내기 1초 전')
    return requestLogin(`/auth/login/?code=${data}`)
  },

  logout: () => {
    console.log('로그아웃 axios 보내기 1초 전')
    return requestPost('auth/logout')
  }

};

export default authApi;