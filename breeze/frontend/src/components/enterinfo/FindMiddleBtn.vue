<template>
  <div class="find-middle-btn">
    <button
      type="button"
      @click="goToFindMiddle()"
      >중간 장소 찾기</button>
  </div>
</template>

<script>
export default {
  name: 'FindMiddleBtn',
  methods: {
    goToFindMiddle: function() {
      this.$router.push({ name: 'FindMiddle' })
    }
  }
}
</script>

<style scoped>
.find-middle-btn {
  position: relative;
}
.find-middle-btn button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 65%;
  height: 65%;
  padding: 3%;
  background: linear-gradient(to left, #92a3fd, #9dceff);
  box-shadow: 1px 1px 5px 0px gray;
  border: none;
  border-radius: 20px;
  color: white;
  font-weight: 600;
}
</style>