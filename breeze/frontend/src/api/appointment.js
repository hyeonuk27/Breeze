import  { requestGet, requestDelete } from '@/utils/request.js';
import SERVER from './drf.js';

export const appointmentApi = {
  
  getAppointmentList: () => {
    return requestGet('/appointments/');
  },
  deleteAppointment: (data) => {
    return requestDelete('/appointment/note/' + `${data.secretCode}/`);
  },
  getAppointment: (id) => {
    console.log('약속쪽지 조회 axios 보내기 1초 전')
    return requestGet(SERVER.ROUTES.appointment + `/${id}`)
  }

};

export default appointmentApi;