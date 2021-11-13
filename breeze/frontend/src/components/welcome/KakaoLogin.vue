<template>
  <div>
    <a :href="auth.url">
      <img src="@/assets/welcome/login.png" alt="" class="kakao-btn-img" />
    </a>
  </div>
</template>

<script>
import { KAKAO_AUTH_URL } from "@/Oauth.js"

export default {
  name: "KakaoLogin",
  data() {
    return {
      auth: { url: KAKAO_AUTH_URL },
    }
  },
}
</script>

<style scoped>
.kakao-btn-img {
  width: 180px;
}
</style>