import  { requestGet, requestDelete } from '@/utils/request.js'
import SERVER from './drf.js'

export const appointmentApi = {

  getAppointment: (id) => {
    return requestGet(SERVER.ROUTES.appointment + `/${id}`)
  },

  getAppointmentList: () => {
    return requestGet('/appointments/')
  },

  deleteAppointment: (data) => {
    return requestDelete('/appointment/note/' + `${data.secretCode}/`)
  }

}

export default appointmentApi