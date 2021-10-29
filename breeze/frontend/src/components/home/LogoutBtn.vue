<template>
  <div class="button-box">
    <button @click="logout">로그아웃</button>
  </div>
</template>

<script>
import authApi from '@/api/auth.js'

export default {
  name: 'LogoutBtn',
  methods: {
    async logout() {
      let accessToken = sessionStorage.getItem("access-token");
      console.log(accessToken, '로그아웃시 액세스토큰')
      const userId = this.$store.getters.getUserId
      const response = await authApi.logout(userId, {
          Authorization: `Bearer ${accessToken}`
      })
      console.log(response, '로그아웃 response')
      if (response.data == 'success') {
        await this.$store.dispatch('removeUser')
        sessionStorage.clear()
        // this.$router.push('/home')
      }
      
    }
  }
}
</script>

<style scoped>
* {
    color: #7B6F72;
    font-size: 14px;
}
  .button-box {
  grid-column: 4;
  grid-row: 1;
  }
  button {
    background-color: rgba(256, 256, 256, 0);
    border: none;
    font-size: 13px;
  }
</style>