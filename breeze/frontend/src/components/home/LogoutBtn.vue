<template>
  <div class="logout-button">
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
      let refreshToken = sessionStorage.getItem("refresh-token");
      const payload = {
        "access-token": accessToken,
        "refresh-token": refreshToken,
      }
      const response = await authApi.logout(payload)
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
  .logout-button {
    grid-column: 4;
    grid-row: 1;
  }
  .logout-button button {
    background-color: rgba(256, 256, 256, 0);
    border: none;
    font-size: 12px;
    color: #7B6F72;
  }
</style>