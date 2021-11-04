<template>
  <swiper class="swiper">
    <Group
      v-for="(group, idx) in groups"
      :key="idx"
      :idx="idx"
      :group="group"
      class="group-box"
    />
  </swiper>
</template>

<script>
import Group from '@/components/oneclick/Group.vue'
import { Swiper } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  name: 'GroupList',
  components: {
    Group,
    Swiper
  },
  data () {
    return {
      groups: [
        {
          'group_name': '행복이들',
          'group_id': 0,
          'group_members': [
            {
              'name': '수빙수빙수빙',
              'building': '멀티캠퍼스 역삼',
            },
            {
              'name': '지미니미니',
              'building': '멀티캠퍼스 역삼',
            },
            {
              'name': '현욱킴',
              'building': '행복하우스',
            },
            {
              'name': '수빈수',
              'building': '멀티캠퍼스 종로',
            },
            {
              'name': '채으니',
              'building': '하우스해피',
            },
            {
              'name': '교저스',
              'building': '하우스행복',
            }
          ]
        },
        {
          'group_name': '뽀로로모임',
          'group_id': 1,
          'group_members': [
            {
              'name': '뽀로로',
              'building': '남극',
            },
            {
              'name': '루피',
              'building': '세종기지',
            },
            {
              'name': '에디',
              'building': '북극',
            }
          ]
        },
        {
          'group_name': '뽀로로모임',
          'group_id': 2,
          'group_members': [
            {
              'name': '뽀로로',
              'building': '남극',
            },
            {
              'name': '루피',
              'building': '세종기지',
            },
            {
              'name': '에디',
              'building': '북극',
            }
          ]
        }
      ]
    }
  }

}
</script>

<style lang="scss" scoped>
.group-box {
  background-color: rgb(157, 206, 255, 0.2);
  border-radius: 15px;
  /* margin: 0 6%; */
  padding: 7%;
  height: 95%;
}
</style>