<template>
  <div id="app">
    <Header v-if="$route.name !== 'Welcome'" id="header"/>
    <router-view :style="[$route.name == 'Welcome' ? {height:'100%'} : {height:'82%'}]"/>
    <Footer v-if="$route.name !== 'Welcome'" id="footer"/>
  </div>
</template>

<script>
import Header from '@/components/common/Header'
import Footer from '@/components/common/Footer'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>

<style>
  @font-face {
    font-family: 'NanumBarunGothic';
    font-style: normal;
    src: url('//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.eot');
    src: url('//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.eot?#iefix') format('embedded-opentype'), url('//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.woff') format('woff'), url('//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.ttf') format('truetype');
  }
  #app {
    font-family: NanumBarunGothic;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    width: 100vw;
    height: 100vh;
  }
  /* 스크롤 */
  ::-webkit-scrollbar {
    width: 5px;
    border-radius: 5px;
  }
  ::-webkit-scrollbar-thumb {
    background-color: #9ABFFF;
    border-radius: 6px;
  }
  ::-webkit-scrollbar-track {
    background-color: rgba(234, 238, 255, 0.7); 
    border-radius: 5px;
  }
  #header {
    height: 9%;
    background: #B8D2FA;
  }
  #footer {
    height: 9%;
    background: #B8D2FA;
  }
</style>
