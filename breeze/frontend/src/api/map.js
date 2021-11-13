import  { requestPost } from '@/utils/request.js'

const mapApi = {

  getPlaceList: (data) => {
    return requestPost('/store/' + `${data.categoryType}/` + `${data.filterType}/`, data)
  },

  middle: (data) => {
    return requestPost('/middle/', data)
  },

  saveAppointment: (data) => {
    return requestPost('/appointment/', data)
  },

}

export default mapApi