<template>
  <swiper class="swiper" ref="groupList" @slide-change-transition-end="getActive">
    <Group
      v-for="(group, idx) in groups"
      :key="idx"
      :idx="idx"
      :group="group"
      class="group-box"
      @renew-grouplist="renewGroupList"
    />
  </swiper>
</template>

<script>
import Group from '@/components/oneclick/Group.vue'
import { Swiper } from 'vue-awesome-swiper'
import { mapActions } from 'vuex'
import 'swiper/css/swiper.css'
import groupApi from '@/api/group.js'

export default {
  name: 'GroupList',
  components: {
    Group,
    Swiper
  },
  data () {
    return {
      // groups: [],
      // enterinfo에서 참여자 저장하는 형식과 맞춘 리스트 
      groupMemInfoList: [],
      groups: [
        {
          'group_name': '행복이들',
          'group_id': 0,
          'group_members': [
            {
              'name': '수빙수빙수빙',
              'building': '멀티캠퍼스 역삼',
              'latitude': '37.559830',
              'longitude': '126.942633',
              'barami_type': 0
            },
            {
              'name': '지미니미니',
              'building': '멀티캠퍼스 역삼',
              'latitude': '37.484232',
              'longitude': '126.929814',
              'barami_type': 1
            },
            {
              'name': '현욱킴',
              'building': '행복하우스',
              'latitude': '',
              'longitude': '',
              'barami_type': 2
            },
            {
              'name': '수빈수',
              'building': '멀티캠퍼스 종로',
              'latitude': '',
              'longitude': '',
              'barami_type': 3
            },
            {
              'name': '채으니',
              'building': '하우스해피',
              'latitude': '37.484232',
              'longitude': '126.929814',
              'barami_type': 4
            },
            {
              'name': '교저스',
              'building': '하우스행복',
              'latitude': '',
              'longitude': '',
              'barami_type': 5
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
              'latitude': '',
              'longitude': '',
              'barami_type': 0
            },
            {
              'name': '루피',
              'building': '세종기지',
              'latitude': '',
              'longitude': '',
              'barami_type': 1
            },
            {
              'name': '에디',
              'building': '북극',
              'latitude': '',
              'longitude': '',
              'barami_type': 2
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
              'latitude': '',
              'longitude': '',
              'barami_type': 0
            },
            {
              'name': '루피',
              'building': '세종기지',
              'latitude': '',
              'longitude': '',
              'barami_type': 3
            },
            {
              'name': '에디',
              'building': '북극',
              'latitude': '',
              'longitude': '',
              'barami_type': 5
            }
          ]
        }
      ],
      activeIndex: 0
    }
  },
  methods: {
    ...mapActions([
      'setParticipants',
      'setGroupName',
      'setGroupId'
    ]),
    getActive () {
      // console.log('바뀌었다')
      const swiper = this.$refs.groupList.$swiper
      this.activeIndex = swiper.activeIndex
      // console.log(this.activeIdx)
    },
    async getGroups () {
      const response = await groupApi.getGroupList()
      console.log(response.group_data, '그룹 리스트 잘 들어왔는지 확인')
      this.groups = response.group_data
    },
    setGroupMemInfo (groupMembers) {
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
      // console.log(this.groupMemInfoList, '형식이 바뀌었는가?')
    },
    setStore (selectedGroup) {
      this.setParticipants(this.groupMemInfoList)
      this.setGroupName(selectedGroup.group_name)
      this.setGroupId(selectedGroup.group_id)
    },
    renewGroupList () {
      // this.getGroups()
      const selectedGroup = this.groups[this.activeIndex]
      this.setGroupMemInfo(selectedGroup.group_members)
      this.setStore(selectedGroup)
    }
  },
  created() {
    // this.getGroups()
    const selectedGroup = this.groups[this.activeIndex]
    this.setGroupMemInfo(selectedGroup.group_members)
    this.setStore(selectedGroup)
  },
  computed: {
    activeIdx () {
      return this.activeIndex
    }
  },
  watch: {
    activeIdx (val) {
      const selectedGroup = this.groups[val]
      this.setGroupMemInfo(selectedGroup.group_members)
      this.setStore(selectedGroup)
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