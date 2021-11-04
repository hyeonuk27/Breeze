<template>
  <div>
    <div id="place-map"></div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "PlaceMap",
  data() {
    return {
      // 카카오맵
      mapContainer: 0,
      wishPlaceList: [],
      placeList: [
        {
          name: "마포소금구이",
          score: 4.2,
          review: 155,
          address: "서울특별시 마포구 합정동 양화로 27",
          latitude: 37.54937608742442,
          phone: "02-324-2198",
          longitude: 126.91234702787905,
          kakao_url: "https://place.map.kakao.com/17600274",
        },
        // {
        //   name: "교다이야",
        //   score: 4.2,
        //   review: 787,
        //   address: "서울특별시 마포구 합정동 성지길 39 빌딩 1층",
        //   phone: "02-544-2298",
        //   latitude: 37.547079397998644,
        //   longitude: 126.91301221571476,
        //   kakao_url: "https://place.map.kakao.com/17600274",
        // },
        // {
        //   name: "우동 카덴",
        //   score: 3.9,
        //   review: 984,
        //   address: "서울특별시 마포구 서교동 양화로7안길 2-1",
        //   phone: "02-366-4248",
        //   latitude: 37.55192788156713,
        //   longitude: 126.91487903318917,
        //   kakao_url: "https://place.map.kakao.com/17600274",
        // },
        // {
        //   name: "오스테리아샘킴",
        //   score: 4.1,
        //   review: 353,
        //   address: "서울특별시 마포구 합정동 양화로3길 55",
        //   phone: "02-321-1198",
        //   latitude: 37.55160471820185,
        //   longitude: 126.91089245335263,
        //   kakao_url: "https://place.map.kakao.com/17600274",
        // },
        // {
        //   name: "동무밥상",
        //   score: 3.9,
        //   review: 384,
        //   address: "서울특별시 마포구 합정동 양화진길 10",
        //   phone: "02-754-5598",
        //   latitude: 37.54856605316061,
        //   longitude: 126.91246430159401,
        //   kakao_url: "https://place.map.kakao.com/17600274",
        // },
      ],
    };
  },
  methods: {
    initMap() {
      var container = document.getElementById("place-map");
      var options = {
        center: new kakao.maps.LatLng(37.54906931328577, 126.91403035281367),
        // center: new kakao.maps.LatLng(this.middleLatitude, this.middleLongitude),
        level: 5,
      };
      var map = new kakao.maps.Map(container, options);
      this.addMiddleMarker(map);
      this.addPlaceMarker(map);
    },
    // 중간 지점 마커 표시
    addMiddleMarker(map) {
      var middleMarkerSrc = require("@/assets/map/middle.png");
      var middelMarkerSize = new kakao.maps.Size(40, 40);
      var middleMarkerImage = new kakao.maps.MarkerImage(
        middleMarkerSrc,
        middelMarkerSize
      );
      var middleMarkerPosition = new kakao.maps.LatLng(
        37.54906931328577,
        126.91403035281367
      );
      // var middleMarkerPosition = new kakao.maps.LatLng(this.middleLatitude, this.middleLongitude)

      var middleMarker = new kakao.maps.Marker({
        // 마커 생성
        map: map, // 마커를 표시할 지도
        image: middleMarkerImage, // 마커 이미지
        position: middleMarkerPosition, // 마커를 표시할 위치
      });
      middleMarker.setMap(map);
    },
    // 장소 마커 표시
    addPlaceMarker(map) {
      for (var i = 0; i < this.placeList.length; i++) {
        var placeMarkerSrc = require("@/assets/map/" + this.mode2 + ".png");
        var placeMarkerSize = new kakao.maps.Size(30, 30);
        var placeMarkerImage = new kakao.maps.MarkerImage(
          placeMarkerSrc,
          placeMarkerSize
        );
        var placeMarkerPosition = new kakao.maps.LatLng(
          this.placeList[i].latitude,
          this.placeList[i].longitude
        );

        var placeMarker = new kakao.maps.Marker({
          map: map,
          image: placeMarkerImage,
          position: placeMarkerPosition,
        });

        placeMarker.setMap(map);

        const score = this.placeList[i].score * 20 + 1.5;
        
        var content = `<div class="wrap">`;
        content +=  `<div class="head">`;
        content +=    `<div class="name">${this.placeList[i].name}</div>`;
        content +=    `<img class="add" src="${require('@/assets/map/add.png')}" alt="">`;
        content +=  `</div>`;
        content +=  `<div class="body">`
        content +=    `<div class="star-ratings">`
        content +=      `<div class="star-ratings-fill" style="width: ${score}%"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>`;
        content +=      `<div class="star-ratings-base"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>`;
        content +=    `</div>`;
        content +=    `<div class="star-ratings-text">(${this.placeList[i].score}) | 리뷰 ${this.placeList[i].review}개<div>`;
        content +=    `<div>${this.placeList[i].address}</div>`;
        content +=    `<div class="desc">${this.placeList[i].phone}</div>`;
        content +=    `<a class="desc" href="${this.placeList[i].kakao_url}">상세보기</a>`;
        content +=  `</div>`;
        content += `</div>`;

        var customOverlay = new kakao.maps.CustomOverlay({
          map: map,
          position: placeMarkerPosition,
          content: content,
          xAnchor: 0.5,
          yAnchor: 1.1,
          clickable: true,
        });

        kakao.maps.event.addListener(placeMarker, "click", function () {
          customOverlay.setMap(map);
        });
        // function closeOverlay() {
        // customOverlay.setMap(null);
      }
    },
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap()
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
      mode2: (state) => state.mode.mode2,
      filter: (state) => state.mode.filter,
      middleLatitude: (state) => state.appointment.middleLatitude,
      middleLongitude: (state) => state.appointment.middleLongitude,
    }),
  },
  watch: {
    mode2(val) {
      console.log("변경", val);
      this.initMap();
    },
  },
};
</script>

<style>
#place-map {
  height: 100%;
  width: 100%;
}
.wrap {
  position: absolute;
  left: 20px;
  bottom: 40px;
  width: 180px;
  height: 80px;
  margin-left: -144px;
  text-align: left;
  overflow: hidden;
  color: #3A3C3C;
  background: rgba(184, 208, 250, 0.7);
  border-radius: 10px;
}
.head {
  width: 100%;
  height: 32%;
  font-size: 11px;
  font-weight: bold;
  overflow: hidden;
  display: flex;
  justify-content: space-between;
  padding: 5% 5% 0 5%;
}
.head img {
  height: 70%;
}
.body {
  width: 100%;
  height: 68%;
  font-size: 10px;
  overflow: hidden;
  padding: 0 5% 5% 5%;
}
.body .desc {
  display: inline;
  margin-right: 5%;
}
.star-ratings {
  display: inline-block;
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
}
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
  .star-ratings-base {
    z-index: 0;
    padding: 0;
    -webkit-text-fill-color: rgb(172, 172, 172);
  }
.star-ratings-text {
  display: inline;
  font-size: 9px;
}


</style>