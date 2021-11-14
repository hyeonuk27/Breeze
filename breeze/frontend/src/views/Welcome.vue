<template>
  <div class="background">
    <img src="@/assets/welcome/wave.png" alt="wave-image" class="wave-background" />
    <img src="@/assets/barami/0.png" alt="barami-0-image" class="barami n0" />
    <img src="@/assets/barami/1.png" alt="barami-1-image" class="barami n1" />
    <img src="@/assets/barami/2.png" alt="barami-2-image" class="barami n2" />
    <img src="@/assets/barami/3.png" alt="barami-3-image" class="barami n3" />
    <img src="@/assets/barami/4.png" alt="barami-4-image" class="barami n4" />
    <img src="@/assets/barami/5.png" alt="barami-5-image" class="barami n5" />
    <div class="about">
      <div class="title">Breeze</div>
      <p class="desc">
        약속 요정 바라미들과 함께 고민 없이<br />
        즐거운 약속을 만들어봐요!
      </p>
    </div>
    <KakaoLogin />
  </div>
</template>

<script>
import KakaoLogin from "@/components/welcome/KakaoLogin.vue"

export default {
  name: "Welcome",
  components: {
    KakaoLogin,
  },
}
</script>

<style scoped>
.about {
  padding-top: 15%;
}
.about .title {
  font-weight: bolder;
  font-size: 35px;
}
.about .desc {
  padding-top: 3%;
  padding-bottom: 2%;
  color: #919399;
  font-weight: bold;
}
.background {
  width: 100vw;
  height: 100vh;
  background-color: #b8d2fa;
}
.barami {
  position: absolute;
  width: 50px;
}
.n0 {
  left: 8.33%;
  top: 39.81%;
}
.n1 {
  left: 23.33%;
  top: 24.69%;
}
.n2 {
  left: 45.56%;
  top: 34.06%;
}
.n3 {
  left: 5.1%;
  top: 16.41%;
}
.n4 {
  right: 16.11%;
  top: 24.69%;
}
.n5 {
  right: 5.11%;
  top: 10%;
}
.wave-background {
  width: 100%;
  height: 45%;
}
</style>