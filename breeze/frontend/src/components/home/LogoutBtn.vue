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
      console.log(accessToken, '로그아웃시 액세스토큰')
      const userId = this.$store.getters.getUserId
      const response = await authApi.logout(userId)
      console.log(response, '로그아웃_프론트에서 받은 응답 확인')
      if (response == 'success') {
        await this.$store.dispatch('removeUser')
        sessionStorage.clear()
        this.$router.push('/')
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