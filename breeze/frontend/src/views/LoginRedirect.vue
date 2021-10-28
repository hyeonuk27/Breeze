<template>
  <div>
    hello.... please.....show 
  </div>
</template>

<script>
import authApi from '@/api/auth.js'

export default {
  name: 'LoginRedirect',
  methods: {
    async kakaoLogin() {
      let code = new URL(window.location.href).searchParams.get('code');
      console.log(code, 'kakao 인가코드 axios 보내기 전 확인')
      const response = await authApi.login(code)
      console.log(response, '로그인 response')
      if (response) {
        await this.$store.dispatch('setUserInfo', 
          // {
          //   nickname: response.nickname
          // }
          {
            nickname: 'jimin'
          }
        )

        this.$router.push('/home')
      }



    }
  },

  created() {
    this.kakaoLogin()
  }

}
</script>

<style>

</style>