import  { requestLogin, requestLogout, requestCheck } from '@/utils/request.js'
import SERVER from './drf.js'

const authApi = {

  check: () => {
    return requestCheck(SERVER.ROUTES.auth + '/check/')
  },

  login: (code) => {
    return requestLogin(SERVER.ROUTES.auth + `/login/?code=${code}`)
  },

  logout: () => {
    return requestLogout(SERVER.ROUTES.auth + '/logout/')
  }

}

export default authApi