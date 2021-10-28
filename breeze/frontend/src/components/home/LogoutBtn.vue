<template>
  <div class="button-box">
    <button>로그아웃</button>
  </div>
</template>

<script>
export default {
  name: 'LogoutBtn',
}
</script>

<style scoped>
  * {
  color: #7B6F72;
  font-size: 14px;
  } 
  .button-box {
  grid-column: 4;
  grid-row: 1;
  }
  button {
    background-color: rgba(256, 256, 256, 0);
    border: none;
    font-size: 13px;
  }
</style>