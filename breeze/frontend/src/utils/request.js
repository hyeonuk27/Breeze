import http from '@/utils/axios.js'
import { setJwtTokens, updateAccessToken, checkAccessToken } from '@/utils/jwt.js'


export const requestLogin = async (url, config) => {
  try {
    const response = await http.get(url, { config })
    if (response.status === 201) {
      if (response.data.access_token) setJwtTokens(response)
      return response.data
    }
    throw new Error()
  } catch (e) {

    throw new Error(e)
  }
}

export const requestLogout = async (url, data, config) => {
  try {
    const response = await http.post(url, data, { config })
    if (response.status === 200) {
      return 'success'
    }
    throw new Error()
  } catch (e) {
    throw new Error(e)
  }
}

export const requestCheck = async (url, config) => {
  try {
    const response = await http.get(url, { config })
    if (response.status === 201) {
      const isExpired = checkAccessToken(response)
      return isExpired
    }
    throw new Error()
  } catch (e) {

    throw new Error(e)
  }
}

export const requestGet = async (url, config) => {
  try {
    const response = await http.get(url, { config })
    if (response.status === 200) {
      if (response.data['access_token']) updateAccessToken(response)
      return response.data
    } else if (response.status === 204) {
      return response.data
    }
    throw new Error()
  } catch (e) {

    throw new Error(e)
  }
}

export const requestPost = async (url, data, config) => {
  try {
    const response = await http.post(url, data, { config })
    if (response.status === 201) {
      if (response.data['access_token']) updateAccessToken(response)
      return response.data
    }
    throw new Error()
  } catch (e) {
    throw new Error(e)
  }
}

export const requestPut = async (url, data, config) => {
  try {
    const response = await http.put(url, data, { config })
    if (response.status === 201) {
      if (response.data['access_token']) updateAccessToken(response)
      return response.data
    }
    throw new Error()
  } catch (e) {
    throw new Error(e)
  }
}

export const requestDelete = async (url, config) => {
  try {
    const response = await http.delete(url, { config })
    if (response.status === 204) {
      if (response.data['access_token']) updateAccessToken(response)
      return 'success'
    }
    throw new Error()
  } catch (e) {
    throw new Error(e)
  }
}
