<template>
  <div class="find-place">
    <Map />
    <WishPlaceList />
    <MakeAppointmentBtn />
  </div>
</template>

<script>
import Map from "@/components/findplace/Map";
import WishPlaceList from "@/components/findplace/WishPlaceList";
import MakeAppointmentBtn from "@/components/findplace/MakeAppointmentBtn";

export default {
  name: 'FindPlace',
  components: {
    Map,
    WishPlaceList,
    MakeAppointmentBtn
  },
}
</script>

<style>
</style>