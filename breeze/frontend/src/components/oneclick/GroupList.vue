<template>
  <swiper
    class="swiper"
    :options="swiperOption"
    ref="groupList"
    @slide-change-transition-start="getActive"
  >
    <Group
      v-for="(group, idx) in groups"
      :key="idx"
      :idx="idx"
      :group="group"
      class="swiper-slide"
      @renew-grouplist="renewGroupList"
    />
    <NoGroup v-if="!groups.length" class="group-box2" />
    <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
</template>

<script>
import NoGroup from "@/components/oneclick/NoGroup.vue"
import Group from "@/components/oneclick/Group.vue"
import { mapActions } from "vuex"
import { Swiper } from "vue-awesome-swiper"
import "swiper/css/swiper.css"

import groupApi from "@/api/group.js"

export default {
  name: "GroupList",
  components: {
    NoGroup,
    Group,
    Swiper,
  },
  data() {
    return {
      activeIndex: 0,
      swiperOption: {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: false,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
          type: "bullets",
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        on: {
          slideChange: this.getActive,
        },
      },
      groupMemInfoList: [],
      groups: [],
    }
  },
  methods: {
    ...mapActions(["setParticipants", "setGroupName", "setGroupId"]),
    getActive() {
      const swiper = this.$refs.groupList.$swiper
      this.activeIndex = swiper.realIndex
    },
    async getGroups() {
      const response = await groupApi.getGroupList()
      this.groups = response.group_data
    },
    setGroupMemInfo(groupMembers) {
      this.groupMemInfoList = []
      for (let i = 0; i < groupMembers.length; i++) {
        const groupMemInfo = {}
        groupMemInfo.baramiType = groupMembers[i].barami_type
        groupMemInfo.partName = groupMembers[i].name
        groupMemInfo.partLocation = groupMembers[i].building
        groupMemInfo.partLatitude = groupMembers[i].latitude
        groupMemInfo.partLongitude = groupMembers[i].longitude
        this.groupMemInfoList.push(groupMemInfo)
      }
    },
    async setGroupInfo() {
      const response = await groupApi.getGroupList()
      this.groups = response.group_data
      if (this.groups.length !== 0) {
        const selectedGroup = this.groups[this.activeIndex]

        const groupMembers = selectedGroup.group_members

        this.groupMemInfoList = []
        for (let i = 0; i < groupMembers.length; i++) {
          const groupMemInfo = {}
          groupMemInfo.baramiType = groupMembers[i].barami_type
          groupMemInfo.partName = groupMembers[i].name
          groupMemInfo.partLocation = groupMembers[i].building
          groupMemInfo.partLatitude = groupMembers[i].latitude
          groupMemInfo.partLongitude = groupMembers[i].longitude
          this.groupMemInfoList.push(groupMemInfo)
        }

        this.setParticipants(this.groupMemInfoList)
        this.setGroupName(selectedGroup.group_name)
        this.setGroupId(selectedGroup.group_id)
      }
    },
    setStore(selectedGroup) {
      this.setParticipants(this.groupMemInfoList)
      this.setGroupName(selectedGroup.group_name)
      this.setGroupId(selectedGroup.group_id)
    },
    renewGroupList() {
      this.setGroupInfo()
    },
  },
  created() {
    this.setGroupInfo()
  },
  computed: {
    activeIdx() {
      return this.activeIndex
    },
  },
  watch: {
    activeIdx(val) {
      const selectedGroup = this.groups[val]
      this.setGroupMemInfo(selectedGroup.group_members)
      this.setStore(selectedGroup)
    },
  },
}
</script>

<style lang="scss" scoped>
.group {
  padding: 9%;
}
.group-list {
  width: 88%;
}
.swiper-slide {
  background-color: rgb(157, 206, 255, 0.2);
  border-radius: 15px;
  padding: 5%;
  height: 95%;
  display: flex;
  flex-direction: column;
}
.swiper-pagination {
  top: 95%;
}
.swiper-pagination-bullet-active {
  background: #94b9f3;
}
</style>