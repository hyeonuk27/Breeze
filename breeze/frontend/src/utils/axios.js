import axios from "axios"
import store from "@/store"
import SERVER from '@/api/drf.js';


axios.defaults.baseURL = SERVER.URL
axios.defaults.headers['Content-Type'] = 'application/json'

axios.interceptors.request.use(
  config => {
    const isAuthenticated = store.getters.getUserId
    console.log(isAuthenticated, '아이디가 있다면=로그인이 되었다면')
    if (isAuthenticated) {
      config.headers.common["Authorization"] = 'Bearer ' + sessionStorage.getItem("access-token");
      console.log(config.headers.common["Authorization"], 'axios 헤더에 날라갈 액세스 토큰')
      config.headers.common["X-Id"] = isAuthenticated;
    }
    return config
  },
  error => {
    Promise.reject(error)
  }
)
axios.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded"

export default axios