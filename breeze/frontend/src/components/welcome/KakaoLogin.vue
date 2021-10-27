<template>
  <div>
    <a :href="auth.url">
      <img src="@/assets/kakao_login.png" alt="" class="kakao-btn-img">
    </a>

  </div>
</template>

<script>
import {KAKAO_AUTH_URL} from '../../Oauth.js';
// import dotenv from "dotenv";
// dotenv.config();

export default {
  name: 'KakaoLogin',
  data() {
    return {
      auth: {url: KAKAO_AUTH_URL}
    }

  },

  methods: {

  },

  // created() {
  //   console.log(process.env)
  //   console.log(process.env.VUE_APP_KAKAO_CLIENT_ID)
  //   console.log(KAKAO_AUTH_URL)
  // }


}
</script>

<style scoped>
.kakao-btn-img {
  width: 180px;
}

</style>