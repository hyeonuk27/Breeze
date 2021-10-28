import  { requestGet, requestDelete } from '@/utils/request.js';
import SERVER from './drf.js';

export const appointmentApi = {
  
  // 약속 리스트 조회
  getAppointmentList: (headers) => {
    return requestGet(SERVER.URL + SERVER.ROUTES.appointment, headers);
  },
  deleteAppointment: (data, headers) => {
    return requestDelete(SERVER.URL + SERVER.ROUTES.appointment + `/${data.nodeId}`, headers);
  }
};

export default appointmentApi;