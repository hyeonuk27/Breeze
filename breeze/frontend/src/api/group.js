import  { requestGet, requestPost, requestDelete } from '@/utils/request.js'
import SERVER from './drf.js'

const groupApi = {

  createGroup: (data) => {
    return requestPost(SERVER.ROUTES.group + '/', data)
  },

  deleteGroup: (id) => {
    return requestDelete(SERVER.ROUTES.group + `/${id}`)
  },

  getGroupList: () => {
    return requestGet('/groups/')
  }
  
}

export default groupApi