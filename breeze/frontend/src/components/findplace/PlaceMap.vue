<template>
  <div>
    <div id="place-map">
      <PlaceMapMiddle />
    </div>
    <PlaceList />
  </div>
</template>

<script>
import PlaceMapMiddle from "@/components/findplace/PlaceMapMiddle";
import PlaceList from "@/components/findplace/PlaceList";
import { mapState } from "vuex";

export default {
  name: "PlaceMap",
  components: {
    PlaceMapMiddle,
    PlaceList,
  },
  data() {
    return {
      placeList: [
        {
          name: '마포소금구이',
          score: 4.2,
          review: 155,
          address: '서울특별시 마포구 합정동 양화로 27',
          latitude: 37.54937608742442,
          longitude: 126.91234702787905,  
        },
        {
          name: '교다이야',
          score: 4.2,
          review: 787,
          address: '서울특별시 마포구 합정동 성지길 39 빌딩 1층',
          latitude: 37.547079397998644,
          longitude: 126.91301221571476 
        },
        {
          name: '우동 카덴',
          score: 3.9,
          review: 984,
          address: '서울특별시 마포구 서교동 양화로7안길 2-1',
          latitude: 37.55192788156713,
          longitude: 126.91487903318917
        },
        {
          name: '오스테리아샘킴',
          score: 4.1,
          review: 353,
          address: '서울특별시 마포구 합정동 양화로3길 55',
          latitude: 37.55160471820185, 
          longitude: 126.91089245335263
        },
        {
          name: '동무밥상',
          score: 3.9,
          review: 384,
          address: '서울특별시 마포구 합정동 양화진길 10',
          latitude: 37.54856605316061, 
          longitude: 126.91246430159401
        },
      ]
    }
  },
  methods: {
    initMap() {
      var container = document.getElementById("place-map");
      var options = {
        center: new kakao.maps.LatLng(37.54906931328577, 126.91403035281367),
        level: 5,
      };

      var map = new kakao.maps.Map(container, options);

      // 마커 이미지의 이미지 주소입니다
      var imageSrc = require('@/assets/map/1.png'); 
      console.log(this.placeList)
          
      for (var i = 0; i < this.placeList.length; i ++) {
          
          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(30, 30); 
          
          // 마커 이미지를 생성합니다    
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
          var markerPosition = new kakao.maps.LatLng(this.placeList[i].latitude, this.placeList[i].longitude)

          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map, // 마커를 표시할 지도
              position: markerPosition, // 마커를 표시할 위치
              image : markerImage // 마커 이미지 
          });

          marker.setMap(map);

      }

    },
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      const apiKey = process.env.VUE_APP_KAKAO_MAP_API_KEY;
      script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${apiKey}`;
      document.head.appendChild(script);
    }
  },
  computed: {
    ...mapState({
      mode2: state => state.appointment.mode2,
      filter: state => state.appointment.filter
    }),
  },
};
</script>

<style>
#place-map {
  height: 100%;
  width: 100%;
}
</style>