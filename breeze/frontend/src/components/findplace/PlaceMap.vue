<template>
<div>
  <PlaceMapMiddle />  
  <PlaceList />  
</div> 
</template>

<script>
import PlaceMapMiddle from "@/components/findplace/PlaceMapMiddle";
import PlaceList from "@/components/findplace/PlaceList";

export default {
  name: 'PlaceMap',
  components: {
    PlaceMapMiddle,
    PlaceList,
  },
}
</script>

<style>

</style>