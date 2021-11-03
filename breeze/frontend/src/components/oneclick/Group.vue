<template>
  <swiper-slide class="group">
    <div class="d-flex justify-content-between align-items-center">
      <div class="group-name">{{ group.group_name }}</div>
      <button type="button" class="btn-close"></button>
    </div>
    <div
    v-for="(member, idx) in group.group_members"
    :key="idx">
      {{ idx }} {{ member }}
    </div>
  </swiper-slide>
</template>

<script>
import { SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  name: 'Group',
  props: {
    group: Object,
    idx: Number,
  },
  components: {
    SwiperSlide
  }

}
</script>

<style scoped>
.group-name {
  font-size: 15pt;
  font-weight: bold;
}
</style>