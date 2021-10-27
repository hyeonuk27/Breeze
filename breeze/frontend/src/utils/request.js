import axios from 'axios';


const setJwtTokens = (response) => {
  if (response.headers['jwt-access-token'])
    sessionStorage.setItem('access-token', response.headers['jwt-access-token']);
  if (response.headers['jwt-refresh-token'])
    sessionStorage.setItem('refresh-token', response.headers['jwt-refresh-token']);
};

// const updateAccessToken = (response) => {
//   if (response.headers['jwt-access-token'] !== sessionStorage.getItem('access-token')) {
//     sessionStorage.setItem('access-token', response.headers['jwt-access-token']);
//   }
// };

export const requestLogin = async (url, headers) => {
  try {
    const response = await axios.get(url, { headers });
    if (response.status === 200) {
      if (response.headers['jwt-access-token']) setJwtTokens(response);
      return response.data;
    }
    throw new Error();
  } catch (e) {

    throw new Error(e);
  }
};