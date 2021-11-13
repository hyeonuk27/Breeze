<template>
  <div class="spinner">
    <div class="bounce bounce1"></div>
    <div class="bounce bounce2"></div>
    <div class="bounce bounce3"></div>
  </div>
</template>

<script>
import authApi from "@/api/auth.js"

export default {
  name: "LoginRedirect",
  methods: {
    async kakaoLogin() {
      let code = new URL(window.location.href).searchParams.get("code")
      const response = await authApi.login(code)
      await this.$store.dispatch("setUser", {
        userId: response.id,
        userName: response.username,
      })
      this.$router.push("/home")
    },
  },
  created() {
    this.kakaoLogin()
  },
}
</script>

<style scoped>
.spinner {
  margin: 100px auto 0;
  width: 100px;
  text-align: center;
}
.spinner .bounce1 {
  -webkit-animation-delay: -0.32s;
  animation-delay: -0.32s;
  margin-right: 10%;
}
.spinner .bounce2 {
  -webkit-animation-delay: -0.16s;
  animation-delay: -0.16s;
  margin-right: 10%;
}
.spinner > div {
  width: 18px;
  height: 18px;
  background-color: #b8d0fa;
  border-radius: 100%;
  display: inline-block;
  -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
  animation: sk-bouncedelay 1.4s infinite ease-in-out both;
}
@-webkit-keyframes sk-bouncedelay {
  0%,
  80%,
  100% {
    -webkit-transform: scale(0);
  }
  40% {
    -webkit-transform: scale(1);
  }
}
@keyframes sk-bouncedelay {
  0%,
  80%,
  100% {
    -webkit-transform: scale(0);
    transform: scale(0);
  }
  40% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}
</style>