<template>
<div>
  <MapMiddle />  
  <MapPlaceList />  
</div> 
</template>

<script>
import MapMiddle from "@/components/findplace/MapMiddle";
import MapPlaceList from "@/components/findplace/MapPlaceList";

export default {
  name: 'Map',
  components: {
    MapMiddle,
    MapPlaceList,
  },
}
</script>

<style>

</style>