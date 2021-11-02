<template>
  <div>
    <!-- <div 
      v-for="(middlePlace, idx) in middlePlaces"
      :key="idx"
    >
      {{ middlePlace }}
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'MiddleList',
  props: {
    middlePlaces: Array
  }

}
</script>

<style>

</style>