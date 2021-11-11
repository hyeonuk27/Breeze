import  { requestGet, requestPost, requestDelete } from '@/utils/request.js';
import SERVER from './drf.js';

const groupApi = {

  getGroupList: () => {
    console.log('그룹 조회 axios 보내기 1초 전')
    return requestGet('/groups/')
  },

  createGroup: (data) => {
    console.log('그룹 생성 axios 보내기 1초 전')
    return requestPost(SERVER.ROUTES.group + '/', data)
  },

  deleteGroup: (id) => {
    console.log('그룹 삭제 axios 보내기 1초 전')
    return requestDelete(SERVER.ROUTES.group + `/${id}`)
  }


};

export default groupApi;