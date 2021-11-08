

export const setJwtTokens = (response) => {
  if (response.data['access_token'])
    sessionStorage.setItem('access-token', response.data['access_token']);
  if (response.data['refresh_token'])
    sessionStorage.setItem('refresh-token', response.data['refresh_token']);
};

export const updateAccessToken = (response) => {
  if (response.data['access_token'] !== sessionStorage.getItem('access-token')) {
    console.log('새로 받은 액세스 토큰으로 업데이트한다')
    sessionStorage.setItem('access-token', response.data['access_token']);
  }
};

export const checkAccessToken = (response) => {
  if (response.data['access_token'] !== sessionStorage.getItem('access-token')) {
    console.log('기존 토큰과 다르다')
    return true
  } 
  return false
};