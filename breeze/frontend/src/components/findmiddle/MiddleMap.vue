<template>
  <div>
    <div id="map" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex"
import mapApi from "@/api/map.js"

export default {
  name: "Map",
  data() {
    return {
      color: ["#f39bab", "#f3cb9b", "#f3e3b3", "#bbd3ab", "#a3d3fb", "#ab9be3"],
      latitude: 0,
      longitude: 0,
      map: null,
      middleIdx: 0,
      modeIdx: 0,
      modeList: [],
      partInfo: [],
    }
  },
  methods: {
    ...mapActions(["setMiddleLists"]),
    concateArray(arr) {
      this.partInfo = []
      const selectedMiddle = arr[this.middleIdx]
      for (let i = 0; i < selectedMiddle.participants.length; i++) {
        for (let j = 0; j < this.participants.length; j++) {
          if (
            selectedMiddle.participants[i].barami_type ===
            this.participants[j].baramiType
          ) {
            this.partInfo.push({
              partLatitude: this.participants[j].partLatitude,
              partLongitude: this.participants[j].partLongitude,
              baramiType: this.participants[j].baramiType,
              partName: this.participants[j].partName,
              time: selectedMiddle.participants[i].time,
              route: selectedMiddle.participants[i].route,
            })
          }
        }
      }
    },
    partAverageTime(data) {
      let temp = []
      let newData = data
      const placeCnt = data.length
      for (let i = 0; i < placeCnt; i++) {
        const partCnt = data[i].participants.length
        for (let j = 0; j < partCnt; j++) {
          temp.push(data[i].participants[j].time)
        }
        const result = temp.reduce(function add(sum, currVal) {
          return sum + currVal
        }, 0)
        const avg = Math.round(result / temp.length)
        newData[i]["avgTime"] = avg
        temp = []
      }
      return newData
    },
    async initMap() {
      const cnt = this.participants.length
      const partBox = []
      for (let i = 0; i < cnt; i++) {
        const part = {
          baramiType: this.participants[i].baramiType,
          partLatitude: this.participants[i].partLatitude,
          partLongitude: this.participants[i].partLongitude,
        }
        partBox.push(part)
      }
      const data = {
        participants: partBox,
        middle_place_type: this.mode,
      }
      const response = await mapApi.middle(data)
      this.modeList = this.partAverageTime(response.middle_data)

      this.setMiddleLists(this.modeList)
      this.concateArray(this.modeList)

      const selectedMiddle = this.modeList[this.middleIdx]
      this.latitude = selectedMiddle.latitude
      this.longitude = selectedMiddle.longitude

      var container = document.getElementById("map")
      var options = {
        center: new kakao.maps.LatLng(this.latitude, this.longitude),
        level: 3,
      }

      var map = new kakao.maps.Map(container, options)

      var bounds = new kakao.maps.LatLngBounds()
      var points = []

      var middleMarkerSrc = require("@/assets/map/middle.png")
      var middelMarkerSize = new kakao.maps.Size(30, 30)
      var middleMarkerImage = new kakao.maps.MarkerImage(
        middleMarkerSrc,
        middelMarkerSize
      )
      var middleMarkerPosition = options.center
      var marker = new kakao.maps.Marker({
        map: map,
        image: middleMarkerImage,
        position: middleMarkerPosition,
      })
      points.push(middleMarkerPosition)
      marker.setMap(map)

      for (var i = 0; i < this.partInfo.length; i++) {
        var partMarkerSrc = require(`@/assets/barami/m${this.partInfo[i].baramiType}.png`)
        var partMarkerSize = new kakao.maps.Size(45, 45)
        var partMarkerImage = new kakao.maps.MarkerImage(
          partMarkerSrc,
          partMarkerSize
        )
        var partMarkerPosition = new kakao.maps.LatLng(
          this.partInfo[i].partLatitude,
          this.partInfo[i].partLongitude
        )

        var partMarker = new kakao.maps.Marker({
          image: partMarkerImage,
          position: partMarkerPosition,
        })
        points.push(partMarkerPosition)
        partMarker.setMap(map)

        var content = `<div class="find-middle-overlay">`
        content += `<div class="desc">`
        content += `<div class="name">${this.partInfo[i].partName}</div>`
        content += `<div class="time">${this.partInfo[i].time}분</div>`
        content += `</div>`
        content += `</div>`

        var customOverlay = new kakao.maps.CustomOverlay({
          map: map,
          position: partMarkerPosition,
          content: content,
          xAnchor: 0.55,
          yAnchor: -0.03,
        })
        customOverlay.setMap(map)

        var linePath = []
        const routesList = this.partInfo[i].route

        for (var j = 0; j < routesList.length; j++) {
          var routesLat = routesList[j][0];
          var routesLng = routesList[j][1];
          linePath.push(new kakao.maps.LatLng(routesLat, routesLng))
        }
        var polyline = new kakao.maps.Polyline({
          path: linePath,
          strokeWeight: 7,
          strokeColor: this.color[this.partInfo[i].baramiType],
          strokeOpacity: 1,
          strokeStyle: "solid",
        })
        polyline.setMap(map)
      }

      for (var k = 0; k < points.length; k++) {
        bounds.extend(points[k])
      }
      map.setBounds(bounds)
    },

    async initMap2() {
      this.concateArray(this.modeList)

      const selectedMiddle = this.modeList[this.middleIdx]
      this.latitude = selectedMiddle.latitude
      this.longitude = selectedMiddle.longitude

      var container = document.getElementById("map")
      var options = {
        center: new kakao.maps.LatLng(this.latitude, this.longitude),
        level: 3,
      }

      var map = new kakao.maps.Map(container, options)

      var bounds = new kakao.maps.LatLngBounds()
      var points = []

      var middleMarkerSrc = require("@/assets/map/middle.png")
      var middelMarkerSize = new kakao.maps.Size(30, 30)
      var middleMarkerImage = new kakao.maps.MarkerImage(
        middleMarkerSrc,
        middelMarkerSize
      )
      var middleMarkerPosition = options.center
      var marker = new kakao.maps.Marker({
        map: map,
        image: middleMarkerImage,
        position: middleMarkerPosition,
      })
      points.push(middleMarkerPosition)
      marker.setMap(map)

      for (var i = 0; i < this.partInfo.length; i++) {
        var partMarkerSrc = require(`@/assets/barami/m${this.partInfo[i].baramiType}.png`)
        var partMarkerSize = new kakao.maps.Size(45, 45)
        var partMarkerImage = new kakao.maps.MarkerImage(
          partMarkerSrc,
          partMarkerSize
        )
        var partMarkerPosition = new kakao.maps.LatLng(
          this.partInfo[i].partLatitude,
          this.partInfo[i].partLongitude
        )

        var partMarker = new kakao.maps.Marker({
          image: partMarkerImage,
          position: partMarkerPosition,
        })
        points.push(partMarkerPosition)
        partMarker.setMap(map)

        var content = `<div class="find-middle-overlay">`
        content += `<div class="desc">`
        content += `<div class="name">${this.partInfo[i].partName}</div>`
        content += `<div class="time">${this.partInfo[i].time}분</div>`
        content += `</div>`
        content += `</div>`

        var customOverlay = new kakao.maps.CustomOverlay({
          map: map,
          position: partMarkerPosition,
          content: content,
          xAnchor: 0.55,
          yAnchor: -0.03,
        })
        customOverlay.setMap(map)

        var linePath = []
        const routesList = this.partInfo[i].route

        for (var j = 0; j < routesList.length; j++) {
          var routesLat = routesList[j][0];
          var routesLng = routesList[j][1];
          linePath.push(new kakao.maps.LatLng(routesLat, routesLng))
        }
        var polyline = new kakao.maps.Polyline({
          path: linePath,
          strokeWeight: 7,
          strokeColor: this.color[this.partInfo[i].baramiType],
          strokeOpacity: 1,
          strokeStyle: "solid",
        })
        polyline.setMap(map)
      }

      for (var k = 0; k < points.length; k++) {
        bounds.extend(points[k])
      }
      map.setBounds(bounds)
    },
    async initMap3() {
      const cnt = this.participants.length
      const partBox = []
      for (let i = 0; i < cnt; i++) {
        const part = {
          baramiType: this.participants[i].baramiType,
          partLatitude: this.participants[i].partLatitude,
          partLongitude: this.participants[i].partLongitude,
        }
        partBox.push(part)
      }
      const data = {
        participants: partBox,
        middle_place_type: this.mode,
      }
      const response = await mapApi.middle(data)
      this.modeList = this.partAverageTime(response.middle_data)

      this.setMiddleLists(this.modeList)
      this.concateArray(this.modeList)

      const selectedMiddle = this.modeList[this.middleIdx]
      this.latitude = selectedMiddle.latitude
      this.longitude = selectedMiddle.longitude

      var container = document.getElementById("map")
      var options = {
        center: new kakao.maps.LatLng(this.latitude, this.longitude),
        level: 3,
      }

      var map = new kakao.maps.Map(container, options)

      var bounds = new kakao.maps.LatLngBounds()
      var points = []

      var middleMarkerSrc = require("@/assets/map/middle.png")
      var middelMarkerSize = new kakao.maps.Size(30, 30)
      var middleMarkerImage = new kakao.maps.MarkerImage(
        middleMarkerSrc,
        middelMarkerSize
      )
      var middleMarkerPosition = options.center
      var marker = new kakao.maps.Marker({
        map: map,
        image: middleMarkerImage,
        position: middleMarkerPosition,
      })
      points.push(middleMarkerPosition)
      marker.setMap(map)

      for (var i = 0; i < this.partInfo.length; i++) {
        var partMarkerSrc = require(`@/assets/barami/m${this.partInfo[i].baramiType}.png`)
        var partMarkerSize = new kakao.maps.Size(45, 45)
        var partMarkerImage = new kakao.maps.MarkerImage(
          partMarkerSrc,
          partMarkerSize
        )
        var partMarkerPosition = new kakao.maps.LatLng(
          this.partInfo[i].partLatitude,
          this.partInfo[i].partLongitude
        )

        var partMarker = new kakao.maps.Marker({
          image: partMarkerImage,
          position: partMarkerPosition,
        })
        points.push(partMarkerPosition)
        partMarker.setMap(map)

        var content = `<div class="find-middle-overlay">`
        content += `<div class="desc">`
        content += `<div class="name">${this.partInfo[i].partName}</div>`
        content += `<div class="time">${this.partInfo[i].time}분</div>`
        content += `</div>`
        content += `</div>`

        var customOverlay = new kakao.maps.CustomOverlay({
          map: map,
          position: partMarkerPosition,
          content: content,
          xAnchor: 0.55,
          yAnchor: -0.03,
        })
        customOverlay.setMap(map)

        var linePath = []
        const routesList = this.partInfo[i].route

        for (var j = 0; j < routesList.length; j++) {
          var routesLat = routesList[j][0]
          var routesLng = routesList[j][1]
          linePath.push(new kakao.maps.LatLng(routesLat, routesLng))
        }
        var polyline = new kakao.maps.Polyline({
          path: linePath,
          strokeWeight: 7,
          strokeColor: this.color[this.partInfo[i].baramiType],
          strokeOpacity: 1,
          strokeStyle: "solid",
        })
        polyline.setMap(map)
      }

      for (var k = 0; k < points.length; k++) {
        bounds.extend(points[k])
      }
      map.setBounds(bounds)
    },

    async sendAxios() {
      const cnt = this.participants.length
      const partBox = []
      for (let i = 0; i < cnt; i++) {
        const part = {
          baramiType: this.participants[i].baramiType,
          partLatitude: this.participants[i].partLatitude,
          partLongitude: this.participants[i].partLongitude,
        }
        partBox.push(part)
      }
      const data = {
        participants: partBox,
        middle_place_type: this.mode,
      }
      const response = await mapApi.middle(data)
      this.modeList = this.partAverageTime(response.middle_data)
      this.setMiddleLists(this.modeList)
    },
    async waitAndRun() {
      await this.sendAxios()
      this.initMap()
    },
  },
  created() {
    this.modeIdx = this.mode
    this.middleIdx = this.middle
    this.modeList = this.middleLists
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap()
    } else {
      const script = document.createElement("script")
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap)
      const apiKey = process.env.VUE_APP_KAKAO_MAP_API_KEY
      script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${apiKey}`
      document.head.appendChild(script)
    }
  },
  computed: {
    ...mapState({
      mode: (state) => state.mode.mode1,
      middle: (state) => state.mode.middle,
    }),
    ...mapGetters(["participants", "middleLists"]),
  },
  watch: {
    mode: function (newVal) {
      this.modeIdx = newVal
      this.initMap()
    },
    middle: function (newVal) {
      this.middleIdx = newVal
      this.initMap2()
    },
  },
}
</script>

<style>
.find-middle-overlay {
  background-color: #b8d2fa;
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