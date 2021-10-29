import axios from 'axios';
import SERVER from '@/api/drf.js';

axios.defaults.baseURL = SERVER.URL


const setJwtTokens = (response) => {
  if (response.data['access_token'])
    sessionStorage.setItem('access-token', response.data['access_token']);
  if (response.data['refresh_token'])
    sessionStorage.setItem('refresh-token', response.data['refresh_token']);
};

const updateAccessToken = (response) => {
  if (response.data['access_token'] !== sessionStorage.getItem('access-token')) {
    sessionStorage.setItem('access-token', response.data['access_token']);
  }
};

export const requestLogin = async (url, headers) => {
  try {
    const response = await axios.get(url, { headers });
    console.log(response, '여기서 잠시 멈추자')
    if (response.status === 201) {
      console.log('응답 성공')
      console.log(response.data['access_token'], '액세스토큰')
      if (response.data.access_token) setJwtTokens(response)
      return response.data;
    }
    throw new Error();
  } catch (e) {

    throw new Error(e);
  }
};

export const requestGet = async (url, headers) => {
  try {
    const response = await axios.get(url, { headers });
    if (response.status === 201) {
      if (response.data['access_token']) updateAccessToken(response);
      return response.data;
    }
    throw new Error();
  } catch (e) {

    throw new Error(e);
  }
};

export const requestPost = async (url, data, headers) => {
  console.log(url, 'url은 어떻게 나오는 지 보자')
  console.log(headers, '내가 바라는 대로 헤더가 들어가니')
  try {
    const response = await axios.post(url, data, { headers });
    if (response.status === 201) {
      if (response.data['access_token']) updateAccessToken(response);
      return response.data;
    }
    throw new Error();
  } catch (e) {
    throw new Error(e);
  }
};

export const requestPut = async (url, data, headers) => {
  try {
    const response = await axios.put(url, data, { headers });
    if (response.status === 201) {
      if (response.data['access_token']) updateAccessToken(response);
      return response.data;
    }
    throw new Error();
  } catch (e) {
    throw new Error(e);
  }
};

export const requestDelete = async (url, headers) => {
  try {
    const response = await axios.delete(url, { headers });
    if (response.status === 201) {
      if (response.data['access_token']) updateAccessToken(response);
      return response.data;
    }
    throw new Error();
  } catch (e) {
    throw new Error(e);
  }
};
