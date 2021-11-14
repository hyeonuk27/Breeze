<template>
  <div>
    <div class="no-group-text">
      <div class="img-box">
        <img class="img" src="@/assets/barami/baramis.png" alt="barami-image" />
      </div>
      <div>아직 저장된 그룹이 없습니다</div>
      <div>약속을 만들러 떠나볼까요?</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NoGroup",
}
</script>

<style scoped>
.img {
  width: 100%;
  height: 100%;
}
.img-box {
  width: 70%;
  margin-left: auto;
  margin-right: auto;
  padding-bottom: 4%;
}
.no-group-text {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>