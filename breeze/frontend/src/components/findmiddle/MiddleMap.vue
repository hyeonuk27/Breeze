<template>
  <div>
    <!-- <div id="map" style="width:360px;height:300px;"></div> -->
    <div id="map" style="width:100%;height:100%;"></div>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
  name: 'Map',
  props: {
    middlePlaces: Array
  },
  data() {
    return {
      //props로 받은 전체 중간 장소 리스트
      middleList: this.middlePlaces,
      //모드에 따라 분류된 중간 장소 리스트
      modeList: [],
      //중간장소 정해진 후, 참여자들의 정보 리스트
      partInfo: [],
      modeIdx: 0,
      middleIdx: 0,
      latitude: 0,
      longitude: 0,
    }
  },
  methods: {
    filterList(modeIdx) {
      this.modeList = []
      for (let i = 0; i < this.middleList.length; i++) {
        if (this.middleList[i].middle_place_type === modeIdx) {
          this.modeList.push(this.middleList[i])         
        }
      }
      return this.modeList
    },
    concateArray(arr) {
      this.partInfo = []
      const selectedMiddle = arr[this.middleIdx]
      for (let i = 0; i < selectedMiddle.participants.length; i++) {
        for (let j = 0; j < this.participants.length; j++) {
          if (selectedMiddle.participants[i].barami_type === this.participants[j].baramiType) {
            this.partInfo.push({
              "partLatitude": this.participants[j].partLatitude,
              "partLongitude": this.participants[j].partLongitude,
              "baramiType": this.participants[j].baramiType,
              "partName": this.participants[j].partName,
              "time": selectedMiddle.participants[i].time
            })
          }
        }
      }
      // console.log(this.partInfo, '참여자 정보')

    },
    initMap() {
      const modes = this.filterList(this.modeIdx)
      this.concateArray(modes)

      const selectedMiddle = modes[this.middleIdx]
      console.log(selectedMiddle, '중간장소 확인')
      this.latitude = selectedMiddle.latitude
      this.longitude = selectedMiddle.longitude
      

      var container = document.getElementById('map');
      var options = {
        center: new kakao.maps.LatLng(this.latitude, this.longitude),
        level: 3,
        // draggable: true
      };

      var map = new kakao.maps.Map(container, options);
      
      var bounds = new kakao.maps.LatLngBounds()
      var points = []
      
      // var middleMarkerSrc = require('@/assets/map/middle.png')
      var middleMarkerSrc = 'https://previews.123rf.com/images/yupiramos/yupiramos1607/yupiramos160710032/60037776-%ED%99%94%EC%82%B4%ED%91%9C-%EC%9C%84%EC%B9%98-%ED%95%80-%EC%A0%88%EC%97%B0-%EC%95%84%EC%9D%B4%EC%BD%98-%EB%94%94%EC%9E%90%EC%9D%B8-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EA%B7%B8%EB%9E%98%ED%94%BD.jpg'
      var middelMarkerSize = new kakao.maps.Size(30, 30)
      var middleMarkerImage = new kakao.maps.MarkerImage(middleMarkerSrc, middelMarkerSize)
      var middleMarkerPosition  = options.center
      var marker = new kakao.maps.Marker({
        map: map,
        image: middleMarkerImage,
        position: middleMarkerPosition,
      })
      points.push(middleMarkerPosition)
      marker.setMap(map)


      for (var i = 0; i < this.partInfo.length; i++) {
        console.log(this.partInfo[i], '참여자 정보')

        // var partMarkerSrc = require("@/assets/barami/m" + this.partInfo[i].baramiType + ".png")
        var partMarkerSrc = require(`@/assets/barami/m${this.partInfo[i].baramiType}.png`)
        var partMarkerSize = new kakao.maps.Size(45, 45)
        var partMarkerImage = new kakao.maps.MarkerImage(partMarkerSrc, partMarkerSize)
        var partMarkerPosition = new kakao.maps.LatLng(this.partInfo[i].partLatitude, this.partInfo[i].partLongitude)

        var partMarker = new kakao.maps.Marker({
            // map: map,
            image : partMarkerImage,
            position: partMarkerPosition,
        })
        points.push(partMarkerPosition)
        partMarker.setMap(map)

        var content = `<div class="find-middle-overlay">`;
            content +=  `<div class="desc">`
            content +=    `<div class="name">${this.partInfo[i].partName}</div>`;
            content +=    `<div class="time">${this.partInfo[i].time}분</div>`;
            content +=  `</div>`;
            content += `</div>`;
        
        var customOverlay = new kakao.maps.CustomOverlay({
          map: map,
          position: partMarkerPosition,
          content: content,
          xAnchor: 0.55,
          yAnchor: -0.03,
        })
        customOverlay.setMap(map)
      }

      for (var k = 0; k < points.length; k++) {
        bounds.extend(points[k])
      }
      map.setBounds(bounds)
    },
  },
  created() {
    this.modeIdx = this.mode
    this.middleIdx = this.middle
    // console.log('created')
  },
  mounted() {
  if (window.kakao && window.kakao.maps) {
    this.initMap();
  } else {
    const script = document.createElement('script');
    /* global kakao */
    script.onload = () => kakao.maps.load(this.initMap);
    const apiKey = process.env.VUE_APP_KAKAO_MAP_API_KEY
		script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${apiKey}`
    document.head.appendChild(script);
  }
},
computed: {
    ...mapState({
    mode: state => state.mode.mode1,
    middle: state => state.mode.middle,
  }),
  ...mapGetters([
    'participants'
  ])
},
watch: {
    mode : function (newVal, ) {
      // console.log(newVal, this.middle, '모드랑 중간값 확인')
      this.modeIdx = newVal
      this.initMap()
    },
    middle : function (newVal, ) {
      // console.log(this.mode, newVal, '모드랑 중간값 확인')
      this.middleIdx = newVal
      this.initMap()
    }
  }

}
</script>

<style>
.find-middle-overlay {
  background-color: #B8D2FA;
  width: 120%;
  border-radius: 10px;
}
.find-middle-overlay .desc div {
  font-weight: 900;
  color: #767373;
}
.find-middle-overlay .desc .name {
  padding-top: 4px;
  font-size: 12px;
}
.find-middle-overlay .desc .time {
  font-size: 10px;
}


</style>