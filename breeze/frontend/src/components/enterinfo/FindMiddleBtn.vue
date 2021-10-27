<template>
  <button
    type="button"
    class="btn btn-primary"
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

</style>