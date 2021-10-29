module.exports = {
	devServer: {
      proxy: {
        '/api/v1': {
          target: 'https://k5a202.p.ssafy.io/',
        },
    }
  }
}