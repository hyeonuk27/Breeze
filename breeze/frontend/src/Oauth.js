const CLIENT_ID = process.env.VUE_APP_KAKAO_CLIENT_ID;

// const REDIRECT_URI =  "http://localhost:8080/oauth/kakao/callback";
// const REDIRECT_URI =  "https://k5a202.p.ssafy.io/api/v1/oauth/kakao/callback";
const REDIRECT_URI =  "https://k5a202.p.ssafy.io/oauth/kakao/callback";

export const KAKAO_AUTH_URL = `https://kauth.kakao.com/oauth/authorize?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=code`;