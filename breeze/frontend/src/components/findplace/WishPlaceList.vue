<template>
  <div>
    <WishPlace />
    <div>위시리스트</div>
    <div class="test"></div>
  </div>
</template>

<script>
import WishPlace from "@/components/findplace/WishPlace";

export default {
  name: 'WishPlaceList',
  components: {
    WishPlace
  },
}
</script>

<style>
.test {
  background: white;
  height: 70px;
  width: 70px;
}
</style>