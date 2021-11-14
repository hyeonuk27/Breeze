<template>
  <div class="logout-button">
    <button @click="logout">로그아웃</button>
  </div>
</template>

<script>
import authApi from "@/api/auth.js"

export default {
  name: "LogoutBtn",
  methods: {
    async logout() {
      const userId = this.$store.getters.getUserId
      const response = await authApi.logout(userId)
      if (response == "success") {
        await this.$store.dispatch("removeUser")
        sessionStorage.clear()
        this.$router.push("/")
      }
    },
  },
};
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
  color: #7b6f72;
}
</style>