<template>
  <div class="background">
    <img src="@/assets/wave.png" alt="" class="wave-background">
    <div>Breeze</div>
    <p>약속 요정 바라미들과 함께 고민 없이</p>
    <p>즐거운 약속을 만들어봐요!</p>
    <KakaoLogin/>
  </div>
</template>

<script>
import KakaoLogin from '../components/welcome/KakaoLogin.vue';

export default {
  name: 'Welcome',
  components: {
    KakaoLogin,
  }

}
</script>

<style scoped>
.background {
  width: 100vw;
  height: 100vh;
  background-color: #B8D2FA;
}

.wave-background {
  width: 100%;
  height: 41%;
}

</style>