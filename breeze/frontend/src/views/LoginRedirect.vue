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
      console.log(code, '여기까지 잘 들어오니')
      const response = await authApi.login(code)
      console.log(response, '백이 없으니까 답이 제대로 안오겠지? 에러나려나?')
      if (response) {
        await this.$store.dispatch('setUserInfo', {
          user: response.nickname
        })

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