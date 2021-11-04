<template>
  <div>
    hello.... please.....show 여기에는 나중에 스피너가 들어갈 예정입니다~
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
      console.log(response, '로그인_프론트에서 받은 응답 확인')
      await this.$store.dispatch('setUser', {
        userId: response.id,
        userName: response.username
      })
      this.$router.push('/home')
    }
  },
  created() {
    this.kakaoLogin()
  }

}
</script>

<style>

</style>