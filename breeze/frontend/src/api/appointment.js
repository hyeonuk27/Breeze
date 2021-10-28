import  { requestGet } from '@/utils/request.js';
import SERVER from './drf.js';

export const appointmentApi = {
  
  // 약속 리스트 조회
  getMyAppointmentList: (data, headers) => {
    return requestGet(SERVER.URL + SERVER.ROUTES.appointment, headers);
  },

};

export default appointmentApi;