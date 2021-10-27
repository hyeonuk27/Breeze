<template>
  <div>
    <img src="@/assets/breeze/logo.png" class="logo" alt="breeze-logo">
    <div>안녕하세요 지민님</div>
    <div>약속 요정 바라미들과 즐거운 약속을 만들러 가볼까요!</div>
    <LogoutBtn />
  </div>
</template>

<script>
import LogoutBtn from '@/components/home/LogoutBtn'


export default {
  name: 'Myprofile',
  components: {
    LogoutBtn,
  }
}
</script>

<style>
.logo {
  height: 30px;
}
</style>