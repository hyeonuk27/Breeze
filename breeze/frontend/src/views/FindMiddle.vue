<template>
  <div>
    <MiddleMap :middlePlaces="middlePlaces" class="find-middle"/>
    <MiddleList :middlePlaces="middlePlaces" class="middle-lists"/>
    <FindPlaceBtn :middlePlaces="middlePlaces" class="find-place-btn"/>
  </div>
</template>

<script>
import MiddleMap from '@/components/findmiddle/MiddleMap.vue'
import MiddleList from '@/components/findmiddle/MiddleList.vue'
import FindPlaceBtn from '@/components/findmiddle/FindPlaceBtn.vue'
import mapApi from '@/api/map.js'
import { mapGetters } from 'vuex'

export default {
  name: 'FindMiddle',
  components: {
    MiddleMap,
    MiddleList,
    FindPlaceBtn,
  },
  data() {
    return {
      payload: [],
      // middlePlaces: [],
      middlePlaces : [
        {
          middle_place_type: 0,
          name: '강남역',
          latitude: 37.497926,
          longitude: 127.027553,
          participants: [
            {
              barami_type: 0,
              time: 10
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 70
            },
          ]
        },
        {
          middle_place_type: 0,
          name: '신촌역',
          latitude: 37.559830, 
          longitude: 126.942633,
          participants: [
            {
              barami_type: 0,
              time: 40
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 40
            },
          ]
        },
        {
          middle_place_type: 0,
          name: '신림역',
          latitude: 37.484232,
          longitude: 126.929814,
          participants: [
            {
              barami_type: 0,
              time: 60
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 50
            },
          ]
        },
        {
          middle_place_type: 1,
          name: '광화문역',
          latitude: 37.571603, 
          longitude: 126.976592,
          participants: [
            {
              barami_type: 0,
              time: 90
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 20
            },
          ]
        },
        {
          middle_place_type: 1,
          name: '신촌역',
          latitude: 37.559830, 
          longitude: 126.942633,
          participants: [
            {
              barami_type: 0,
              time: 10
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 25
            },
          ]
        },
        {
          middle_place_type: 1,
          name: '강남역',
          latitude: 37.497926,
          longitude: 127.027553,
          participants: [
            {
              barami_type: 0,
              time: 50
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 21
            },
          ]
        },
        {
          middle_place_type: 2,
          name: '석촌역',
          latitude: 37.505288, 
          longitude: 127.107069,
          participants: [
            {
              barami_type: 0,
              time: 10
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 22
            },
          ]
        },
        {
          middle_place_type: 2,
          name: '강남역',
          latitude: 37.497926,
          longitude: 127.027553,
          participants: [
            {
              barami_type: 0,
              time: 70
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 29
            },
          ]
        },
        {
          middle_place_type: 2,
          name: '신촌역',
          latitude: 37.559830, 
          longitude: 126.942633,
          participants: [
            {
              barami_type: 0,
              time: 0
            },
            {
              barami_type: 1,
              time: 30
            },
            {
              barami_type: 2,
              time: 20
            },
            {
              barami_type: 3,
              time: 19
            },
          ]
        }
      ]
    }
  },
  methods: {
    setData() {
      // console.log(this.participants)
      const cnt = this.participants.length
      for (let i = 0; i < cnt; i++) {
        const part = {
          baramiType: this.participants[i].baramiType,
          partLatitude: this.participants[i].partLatitude,
          partLongitude: this.participants[i].partLongitude
        }
        this.payload.push(part)
      }
      return this.payload


    },
    async findMiddle() {
      const data = await this.setData()
      // console.log(data, '내가 axios에 data로 담아 보내는 정보')
      const response = await mapApi.middle(data)
      console.log(response, '중간 장소 관련 data들이 넘어오겠지')
      // this.middlePlaces = response
    }

  },
   computed: {
    ...mapGetters([
      'participants'
    ])
  },
  created() {
    this.findMiddle()
  }

}
</script>

<style scoped>
.find-middle {
  /* height: 65%; */
  height: 57%;
}
.middle-lists {
  /* height: 21%; */
  height: 29%;
}
.find-place-btn {
  height: 14%;
}
</style>