<template>
  <div>
    <MiddleMap :middlePlaces="middlePlaces"/>
    <MiddleList :middlePlaces="middlePlaces"/>
    <FindPlaceBtn :middlePlaces="middlePlaces"/>
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

<style>

</style>