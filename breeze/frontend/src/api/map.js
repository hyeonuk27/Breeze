import  { requestPost } from '@/utils/request.js';
// import SERVER from './drf.js';

const mapApi = {

  middle: (data) => {
    console.log('중간장소찾기 axios 보내기 1초 전')
    // return requestPost(SERVER.ROUTES.map + '/middle/', data)
    return requestPost('/middle/', data)
  },
  getPlaceList: (data) => {
    return requestPost('/store/' + `${data.categoryType}/` + `${data.filterType}/`, data)
  },
  saveAppointment: (data) => {
    return requestPost('/appointment/', data)
  },
};

export default mapApi;