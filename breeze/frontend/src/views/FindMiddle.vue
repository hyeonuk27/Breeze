<template>
  <div>
    <MiddleList/>
    <FindPlaceBtn/>
  </div>
</template>

<script>
import MiddleList from '@/components/findmiddle/MiddleList.vue'
import FindPlaceBtn from '@/components/findmiddle/FindPlaceBtn.vue'

export default {
  name: 'FindMiddle',
  components: {
    MiddleList,
    FindPlaceBtn,
  }

}
</script>

<style>

</style>