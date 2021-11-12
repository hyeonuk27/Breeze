<template>
  <div>
    <div id="place-map"></div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import mapApi from '@/api/map.js'

export default {
  name: "PlaceMap",
  data() {
    return {
      clickedOveray : null,
      placeList: [],
    };
  },
  methods: {
    ...mapActions([
      'addWishPlace',
      'deleteWishPlace'
    ]),

    async initMap() {
      // 장소 데이터 가져오기
      const data = {
        middlePlace: this.middleName, 
        latitude: this.middleLatitude, 
        longitude: this.middleLongitude,
        categoryType: this.mode2,
        filterType: this.filter, 
      }
      const response = await mapApi.getPlaceList(data)
      this.placeList = response.stores
      
      // 지도 표시
      var container = document.getElementById("place-map");
      var options = {
        center: new kakao.maps.LatLng(this.middleLatitude, this.middleLongitude),
        level: 4,
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
      var middelMarkerSize = new kakao.maps.Size(30, 30);
      var middleMarkerImage = new kakao.maps.MarkerImage(middleMarkerSrc, middelMarkerSize);
      var middleMarkerPosition = new kakao.maps.LatLng(this.middleLatitude, this.middleLongitude)

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
      var placeMarkerSize = new kakao.maps.Size(28, 28);
      var placeMarkerImage = new kakao.maps.MarkerImage(placeMarkerSrc, placeMarkerSize);
      var placeMarkerPosition = new kakao.maps.LatLng(place.latitude, place.longitude);

      var placeMarker = new kakao.maps.Marker({
        map: map,
        image: placeMarkerImage,
        position: placeMarkerPosition,
      });

      var placeOverlay = new kakao.maps.CustomOverlay({
        position: placeMarker.getPosition(),
        clickable: true,
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
      
      var placeAddImg = document.createElement('img')
      placeAddImg.setAttribute('src', require('@/assets/map/add.png'));

      // Wish 담기 이벤트
      placeAddImg.addEventListener('click', () => {
        const wishPlace = {placeName : place.name, placeCategory: place.category_num, placeUrl: place.kakao_url, }
        this.addWishPlace(wishPlace)
      });

      var starRatings = document.createElement('div');
      starRatings.className = "star-ratings"

      var starRatingsText = document.createElement('div')
      starRatingsText.className = "star-ratings-text"
      starRatingsText.innerHTML = '(' + place.rate + ')| 리뷰 ' + place.review + '개';

      const rate = place.rate * 20 + 1.5;
      var starRatingsFill = document.createElement('div')
      starRatingsFill.className = "star-ratings-fill"
      starRatingsFill.style.width = rate + '%'
      
      var starRatingsBase = document.createElement('div')
      starRatingsBase.className = "star-ratings-base"
      
      var star1 = document.createElement('span')
      star1.innerHTML = '★★★★★'
      var star2 = document.createElement('span')
      star2.innerHTML = '★★★★★'

      var placeAddress = document.createElement('div');
      placeAddress.innerHTML = place.address;

      var placePhone = document.createElement('a')
      placePhone.className = "place-desc"
      placePhone.innerHTML = place.phone;
      placePhone.href = 'tel: ' + place.phone

      var placeUrl = document.createElement('a')
      placeUrl.innerHTML = '상세보기'
      placeUrl.className = "place-desc"
      placeUrl.href = place.kakao_url;

      // HTML Element 구성
      placeContent.append(placeHead, placeBody);
      placeHead.append(placeName, placeAddImg)
      placeBody.append(starRatings, starRatingsText, placeAddress, placePhone, placeUrl)
      starRatings.append(starRatingsFill, starRatingsBase)
      starRatingsFill.append(star1)
      starRatingsBase.append(star2)

      // 마커 오버레이에 HTML Element 추가
      placeOverlay.setContent(placeContent);

      // 마커 클릭 이벤트
      kakao.maps.event.addListener(placeMarker, 'click', () => {
        if ( this.clickedOveray ) {
          this.clickedOveray.setMap(null)
        }
        placeOverlay.setMap(map)
        this.clickedOveray = placeOverlay
      })
      // 맵 클릭 이벤트
      kakao.maps.event.addListener(map, 'click', function() {
        placeOverlay.setMap(null)      
      })
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
  computed: {
    ...mapGetters([
      'mode2', 
      'filter',
      'middleName', 
      'middleLatitude', 
      'middleLongitude',
      'wishPlaces',
    ]),
  },
  watch: {
    mode2(val) {
      console.log("모드변경", val);
      this.initMap();
    },
    filter(val) {
      console.log("필터변경", val);
      this.initMap();
    }
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
  width: 180px;
  height: 80px;
  margin-left: -120px;
  text-align: left;
  color: #3a3c3c;
  /* background: rgba(184, 208, 250, 0.9); */
  background: rgba(256, 256, 256, 0.9);
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
}
</style>