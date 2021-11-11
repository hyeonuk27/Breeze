<template>
  <swiper-slide class="group">
    <div class="d-flex justify-content-between align-items-center">
      <div class="group-name">{{ group.group_name }}</div>
      <button type="button" class="btn-close" @click="deleteGroup()"></button>
    </div>
    <div class="row group-container">
      <div
      v-for="(member, idx) in group.group_members"
      :key="idx"
      class="col-4 group-member-container">
        <div class="group-member">
          <div class="image-box">
            <img
              :src="require('@/assets/barami/' + member.barami_type + '.png')"
              class="image-box-barami"
              alt="barami-character"
            />
          </div>
          <div class="member-name">{{ member.name }}</div>
          <div class="member-location">{{ member.building }}</div>
        </div>
      </div>
    </div>
  </swiper-slide>
</template>

<script>
import { SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'
import groupApi from '@/api/group.js'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Group',
  props: {
    group: Object,
    idx: Number,
  },
  components: {
    SwiperSlide
  },
  data() {
    return {
      groupIdx: 0,
    }
  },
  methods: {
     ...mapActions([
      'setParticipants',
      'setGroupName',
      'setGroupId',
    ]),
    async deleteGroup() {
      console.log(this.groupIdx)
      if (confirm('정말 삭제하시겠습니까?')) {
        const response = await groupApi.deleteGroup(this.groupIdx)
        // console.log(response)
        if (response == 'success') {
          this.setParticipants([])
          this.setGroupName('')
          this.setGroupId(null)
          this.$emit('renew-grouplist')
        }
      }
    }
  },
  created() {
    this.groupIdx = this.groupId
  },
  computed: {
  ...mapGetters([
      'groupId',
    ])
  }
}
</script>

<style scoped>
.group-name {
  font-size: 15pt;
  font-weight: bold;
}
.image-box {
  width: 45%;
  margin: 1% auto;
}
.image-box-barami {
  width: 100%;
  height: 100%;
}
.group-container {
  margin: auto;
}
.group-member-container {
  padding-right: 0;
  padding-left: 0;
  padding: 2%;
}
.group-member {
  background-color: rgb(255, 255, 255, 0.8);
  border-radius: 15px;
  height: 100%;
  padding-top: 20%;
  padding-bottom: 20%;
}
.member-name {
  margin-top: 4%;
  font-size: 11pt;
  font-weight: bold;
}
.member-location {
  font-size: 9pt;
  color: #7B6F72;
}
</style>