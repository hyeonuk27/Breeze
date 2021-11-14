<template>
  <div id="app">
    <Header v-if="$route.name !== 'Welcome'" id="header" />
    <router-view
      :style="[
        $route.name == 'Welcome' ? { height: '100%' } : { height: '78%' },
      ]"
    />
    <Footer
      v-if="
        $route.name !== 'Welcome' && $route.name !== 'NotFound' && isLoggedIn
      "
      id="footer"
    />
  </div>
</template>

<script>
import Footer from "@/components/common/Footer"
import Header from "@/components/common/Header"
import { mapGetters } from "vuex"

export default {
  name: "App",
  components: {
    Footer,
    Header,
  },
  computed: {
    ...mapGetters(["isLoggedIn"]),
  },
}
</script>

<style>
#app {
  font-family: NanumBarunGothic;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 100vw; 
  height: 100vh;
}
::-webkit-scrollbar {
  width: 5px;
  border-radius: 5px;
}
::-webkit-scrollbar-thumb {
  background-color: #9abfff;
  border-radius: 6px;
}
::-webkit-scrollbar-track {
  background-color: rgba(234, 238, 255, 0.7);
  border-radius: 5px;
}
#footer {
  height: 9%;
  background: #b8d2fa;
}
#header {
  height: 9%;
  background: #b8d2fa;
}
@font-face {
  font-family: "NanumBarunGothic";
  font-style: normal;
  src: url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.eot");
  src: url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.eot?#iefix")
      format("embedded-opentype"),
    url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.woff")
      format("woff"),
    url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.ttf")
      format("truetype");
}
</style>
