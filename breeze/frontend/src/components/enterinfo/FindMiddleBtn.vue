<template>
  <button
    type="button"
    class="btn btn-primary find-middle-btn"
    @click="goToFindMiddle()"
    >중간 장소 찾기</button>
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

<style>
.find-middle-btn {
  
}
</style>