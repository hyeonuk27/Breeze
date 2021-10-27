import  { requestLogin } from '@/utils/request.js';
// import SERVER from './drf.js';

const authApi = {

  login: (data) => {
    console.log('로그인 axios 보내기 1초 전')
    return requestLogin(`https://k5a202.p.ssafy.io?code=${data}`)
    // return requestLogin(SERVER.URL + SERVER.ROUTES.login + `?code=${data}`)
  }

};

export default authApi;