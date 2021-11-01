import  { requestGet, requestDelete } from '@/utils/request.js';
import SERVER from './drf.js';

export const appointmentApi = {
  
  // 약속 리스트 조회
  getAppointmentList: (headers) => {
    return requestGet(SERVER.ROUTES.appointment, headers);
  },
  deleteAppointment: (data, headers) => {
    return requestDelete(SERVER.ROUTES.appointment + `/${data.nodeId}`, headers);
  }
};

export default appointmentApi;