export const setJwtTokens = (response) => {
  if (response.data['access_token'])
    sessionStorage.setItem('access-token', response.data['access_token'])
  if (response.data['refresh_token'])
    sessionStorage.setItem('refresh-token', response.data['refresh_token'])
}

export const updateAccessToken = (response) => {
  if (response.data['access_token'] !== sessionStorage.getItem('access-token')) {
    sessionStorage.setItem('access-token', response.data['access_token'])
  }
}

export const checkAccessToken = (response) => {
  if (response.data['access_token'] !== sessionStorage.getItem('access-token')) {
    return true
  }
  return false
}