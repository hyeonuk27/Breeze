<template>
  <button
    type="button"
    class="btn btn-primary find-middle-btn"
    @click="goToFindMiddle()"
    >중간 장소 찾기</button>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'FindMiddleBtn',
  methods: {
    ...mapActions([
      'setMode1',
      'setMiddle'
    ]),
    goToFindMiddle: function() {
      this.$router.push({ name: 'FindMiddle' })
      this.setMode1(0)
      this.setMiddle(0)
    }
  }
}
</script>

<style>
.find-middle-btn {
  background: linear-gradient(to left, #92A3FD, #9DCEFF);
  border: none;
  border-radius: 20px;
  padding: 3%;
  width: 65%;
  box-shadow: 1px 1px 5px 0px gray;
}
</style>