import  { requestGet, requestDelete } from '@/utils/request.js';

export const appointmentApi = {
  
  getAppointmentList: () => {
    return requestGet('/appointment/');
  },
  deleteAppointment: (data) => {
    return requestDelete('/appointment/note/' + `${data.secretCode}/`);
  }
};

export default appointmentApi;