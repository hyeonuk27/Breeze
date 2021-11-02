<template>
  <button
    type="button"
    class="btn btn-primary"
    @click="goToFindPlace()"
    >약속 계획 짜기
    </button>
</template>

<script>
export default {
  name: 'FindMiddleBtn',
  props: {
    middlePlaces: Array
  },
  methods: {
    goToFindPlace: function() {
      this.$router.push({ name: 'FindPlace' })
    }
  }
}
</script>

<style>

</style>