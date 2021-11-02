<template>
  <div>
    <div id="map" style="width:500px;height:400px;"></div>
  </div>
</template>

<script>
export default {
  name: 'Map',
  props: {
    middlePlaces: Array
  },
  methods: {
    initMap() {
      var container = document.getElementById('map');
      var options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3
      };

      var map = new kakao.maps.Map(container, options);
      var markerPosition  = new kakao.maps.LatLng(33.450701, 126.570667); 
      var marker = new kakao.maps.Marker({
            position: markerPosition
      });
      marker.setMap(map);
  
      }
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
}

}
</script>

<style>

</style>