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
      isClicked : [false,false,false,false,false,],
      placeList: [
        {
          name: "마포소금구이",
          score: 4.2,
          review: 155,
          address: "서울특별시 마포구 합정동 양화로 27",
          latitude: 37.54937608742442,
          phone: "02-324-2198",
          longitude: 126.91234702787905,
          kakao_url: "https://naver.cafe.com",
        },
        {
          name: "교다이야",
          score: 4.2,
          review: 787,
          address: "서울특별시 마포구 합정동 성지길 39 빌딩 1층",
          phone: "02-544-2298",
          latitude: 37.547079397998644,
          longitude: 126.91301221571476,
          kakao_url: "https://place.map.kakao.com/17600274",
        },
        {
          name: "우동 카덴",
          score: 3.9,
          review: 984,
          address: "서울특별시 마포구 서교동 양화로7안길 2-1",
          phone: "02-366-4248",
          latitude: 37.55192788156713,
          longitude: 126.91487903318917,
          kakao_url: "https://place.map.kakao.com/17600274",
        },
        {
          name: "오스테리아샘킴",
          score: 1.2,
          review: 353,
          address: "서울특별시 마포구 합정동 양화로3길 55",
          phone: "02-321-1198",
          latitude: 37.55160471820185,
          longitude: 126.91089245335263,
          kakao_url: "https://place.map.kakao.com/17600274",
        },
        {
          name: "동무밥상",
          score: 3.9,
          review: 384,
          address: "서울특별시 마포구 합정동 양화진길 10",
          phone: "02-754-5598",
          latitude: 37.54856605316061,
          longitude: 126.91246430159401,
          kakao_url: "https://naver.com",
        },
      ],
    };
  },
  methods: {
    // 지도 표시
    initMap() {
      var container = document.getElementById("place-map");
      var options = {
        center: new kakao.maps.LatLng(37.54906931328577, 126.91403035281367),
        // center: new kakao.maps.LatLng(this.middleLatitude, this.middleLongitude),
        level: 5,
      };
      var map = new kakao.maps.Map(container, options);
      
      this.addMiddleMarker(map);
      for(let i = 0; i < this.placeList.length; i++){
          var place = this.placeList[i];
          this.addPlaceMarker(map, place);
      }
    },
    // 중간 지점 마커 표시
    addMiddleMarker(map) {
      var middleMarkerSrc = require("@/assets/map/middle.png");
      var middelMarkerSize = new kakao.maps.Size(40, 40);
      var middleMarkerImage = new kakao.maps.MarkerImage(middleMarkerSrc, middelMarkerSize);
      var middleMarkerPosition = new kakao.maps.LatLng(37.54906931328577, 126.91403035281367);
      // var middleMarkerPosition = new kakao.maps.LatLng(this.middleLatitude, this.middleLongitude)

      var middleMarker = new kakao.maps.Marker({
        map: map,
        image: middleMarkerImage,
        position: middleMarkerPosition,
      });
      middleMarker.setMap(map);
    },
    // 장소 마커 표시
    addPlaceMarker(map, place) {
      var placeMarkerSrc = require("@/assets/map/" + this.mode2 + ".png");
      var placeMarkerSize = new kakao.maps.Size(30, 30);
      var placeMarkerImage = new kakao.maps.MarkerImage(placeMarkerSrc, placeMarkerSize);
      var placeMarkerPosition = new kakao.maps.LatLng(place.latitude, place.longitude);

      var placeMarker = new kakao.maps.Marker({
        map: map,
        image: placeMarkerImage,
        position: placeMarkerPosition,
      });

      var placeOverlay = new kakao.maps.CustomOverlay({
        map: map,
        position: placeMarker.getPosition(),
      });

      // HTMLElement 생성
      var placeContent = document.createElement('div');
      placeContent.className = "place-content"
      
      var placeHead = document.createElement('div');
      placeHead.className = "place-head"

      var placeBody = document.createElement('div');
      placeBody.className = "place-body"

      var placeName = document.createElement('div')
      placeName.innerHTML = place.name;

      var placeAdd = document.createElement('img')
      placeAdd.setAttribute('src', require('@/assets/map/add2.png'));

      var placeClose = document.createElement('img')
      placeClose.setAttribute('src', require('@/assets/common/close.png'));
      placeClose.onclick = function () {
        placeOverlay.setMap(null);
      };
      var starRatings = document.createElement('div');
      starRatings.className = "star-ratings"

      var starRatingsText = document.createElement('div')
      starRatingsText.className = "star-ratings-text"
      starRatingsText.innerHTML = '(' + place.score + ')| 리뷰 ' + place.review + '개';

      const score = place.score * 20 + 1.5;
      var starRatingsFill = document.createElement('div')
      starRatingsFill.className = "star-ratings-fill"
      starRatingsFill.style.width = score + '%'
      
      var starRatingsBase = document.createElement('div')
      starRatingsBase.className = "star-ratings-base"
      
      var star1 = document.createElement('span')
      star1.innerHTML = '★★★★★'
      var star2 = document.createElement('span')
      star2.innerHTML = '★★★★★'

      var placeAddress = document.createElement('div');
      placeAddress.innerHTML = place.address;

      var placePhone = document.createElement('div')
      placePhone.className = "place-desc"
      placePhone.innerHTML = place.phone;

      var placeUrl = document.createElement('a')
      placeUrl.innerHTML = '상세보기'
      placeUrl.className = "place-desc"
      placeUrl.href = place.kakao_url;

      // HTMLElement 구성
      placeContent.append(placeHead, placeBody);
      placeHead.append(placeName, placeAdd, placeClose)
      placeBody.append(starRatings, starRatingsText, placeAddress, placePhone, placeUrl)
      starRatings.append(starRatingsFill, starRatingsBase)
      starRatingsFill.append(star1)
      starRatingsBase.append(star2)

      // 마커 오버레이에 HTMLElement 추가
      placeOverlay.setContent(placeContent);
      placeOverlay.setMap(null)

      // 마커 클릭 이벤트
    kakao.maps.event.addListener(placeMarker, 'click', function() {
      placeOverlay.setMap(map);
    });
    }
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
  created() {

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
.place-content {
  position: absolute;
  left: 40px;
  bottom: 35px;
  width: 200px;
  height: 80px;
  margin-left: -140px;
  text-align: left;
  overflow: hidden;
  color: #3a3c3c;
  background: rgba(184, 208, 250, 0.9);
  border-radius: 10px;
}
.place-head {
  width: 100%;
  height: 32%;
  font-size: 11px;
  font-weight: bold;
  overflow: hidden;
  display: flex;
  justify-content: space-between;
  padding: 5% 5% 0 5%;
}
.place-head img {
  height: 15px
}
.place-body {
  width: 100%;
  height: 68%;
  font-size: 10px;
  overflow: hidden;
  padding: 0 5% 5% 5%;
}
.place-desc {
  display: inline;
  margin-right: 5%;
}
.star-ratings {
  display: inline-block;
  color: #aaa9a9;
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent;
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