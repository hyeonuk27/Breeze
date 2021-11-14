import axios from "axios"
import store from "@/store"
import SERVER from '@/api/drf.js'


const http = axios.create({
  baseURL: SERVER.URL,
  headers: { "content-type": "application/json" },
})

http.interceptors.request.use(
  config => {
    const isAuthenticated = store.getters.getUserId
    if (isAuthenticated) {
      config.headers.common["Authorization"] = 'Bearer ' + sessionStorage.getItem("access-token")
      config.headers.common["X-Id"] = isAuthenticated
    }
    return config
  },
  error => {
    Promise.reject(error)
  }
)
http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded"

export default http