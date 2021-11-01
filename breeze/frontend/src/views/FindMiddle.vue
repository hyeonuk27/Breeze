<template>
  <div>
    <!-- <MiddleMap/> -->
    <MiddleList/>
    <FindPlaceBtn/>
  </div>
</template>

<script>
// import MiddleMap from '@/components/findmiddle/MiddleMap.vue'
import MiddleList from '@/components/findmiddle/MiddleList.vue'
import FindPlaceBtn from '@/components/findmiddle/FindPlaceBtn.vue'

export default {
  name: 'FindMiddle',
  components: {
    // MiddleMap,
    MiddleList,
    FindPlaceBtn,
  }

}
</script>

<style>

</style>