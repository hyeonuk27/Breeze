<template>
<div class="add-friends-items">
  <div class="add-friends-box">
    <div class="add-friends-title">
      <i class="far fa-user add-friends-icon"></i>친구 추가하기
    </div>
    <input
      type="text"
      class="place-input"
      v-model="searchWord"
      @input="searchPlace"
      ref="place-input-ref"
      placeholder="출발지를 입력해주세요."
    />
    <!-- 출발지 검색 결과 창 -->
    <div v-if="isSearchResultOpen" class="search-result">
      <div v-for="(result, idx) in searchResult" :key="idx">
        <div class="d-flex align-items-center" @click="setLocation(idx)">
          <h3 class="col-2"><i class="fas fa-map-marker-alt"></i></h3>
          <div class="search-item">
            <p class="search-place">{{ result.place_name }}</p>
            <p class="search-address">{{ result.address_name }}</p>
          </div>
        </div>
        <hr class="search-divide" />
      </div>
    </div>
    <div
      class="row d-flex justify-content-between add-friends-name-btn-container"
    >
      <input
        type="text"
        class="col-10 name-input"
        v-model="partName"
        placeholder="이름을 1~6자로 입력해주세요."
      />
      <button @click="addPart" class="col-2 add-friends-btn">
        <i class="fas fa-plus"></i>
      </button>
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios"
import { mapActions, mapGetters } from "vuex"
import Swal from "sweetalert2"

export default {
  name: "AddFriends",
  data() {
    return {
      searchWord: "",
      partName: "",
      searchResult: [],
      partLocation: null,
      partLatitude: null,
      partLongitude: null,
      isSearchResultOpen: false,
    }
  },
  methods: {
    ...mapActions(["addParticipant"]),
    searchPlace() {
      if (this.searchWord.trim()) {
        // 키워드 장소 검색
        const URL = "https://dapi.kakao.com/v2/local/search/keyword.json"
        const apiKey = process.env.VUE_APP_KAKAO_CLIENT_ID
        axios
          .get(URL, {
            headers: {
              Authorization: "KakaoAK " + apiKey,
            },
            params: {
              query: this.searchWord,
            },
          })
          .then((res) => {
            this.isSearchResultOpen = true
            this.searchResult = res.data.documents
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        this.isSearchResultOpen = false
      }
    },
    setLocation(idx) {
      const target = this.searchResult[idx]
      this.partLocation = target.place_name
      this.partLatitude = target.y
      this.partLongitude = target.x
      this.searchWord = target.place_name
      this.searchResult = []
      this.isSearchResultOpen = false
    },
    addPart() {
      if (!this.partLocation || !this.partLocation.trim()) {
        Swal.fire({
          icon: "error",
          html: "<b>출발지를 입력해주세요</b>",
          showConfirmButton: false,
          timer: 1500,
        })
      } else if (!this.partName || !this.partName.trim()) {
        Swal.fire({
          icon: "error",
          html: "<b>이름을 입력해주세요</b>",
          showConfirmButton: false,
          timer: 1500,
        })
      } else if (this.partName.length > 6 || this.partName.trim().length > 6) {
        Swal.fire({
          icon: "error",
          html: "<b>이름은 1~6자로 입력해주세요</b>",
          showConfirmButton: false,
          timer: 1500,
        })
      } else if (this.participants.length == 6) {
        Swal.fire({
          icon: "error",
          html: "<b>친구는 최대 6명까지만 추가가 가능해요</b>",
          showConfirmButton: false,
          timer: 1500,
        })
        this.partName = ""
        this.searchWord = ""
      } else {
        const data = {
          baramiType: this.participants.length,
          partName: this.partName,
          partLocation: this.partLocation,
          partLatitude: this.partLatitude,
          partLongitude: this.partLongitude,
        }
        this.addParticipant(data)
        this.partName = ""
        this.partLocation = null
        this.partLatitude = null
        this.partLongitude = null
        this.searchWord = ""
      }
    },
  },
  computed: {
    ...mapGetters(["participants"]),
  },
}
</script>

<style>

.add-friends-box {
  background-color: #e9edfe;
  border-radius: 15px;
}
.add-friends-btn {
  background: linear-gradient(to left, #92a3fd, #9dceff);
  border: none;
  border-radius: 15px;
  padding: 1.5% 2%;
  color: white;
  font-size: 10pt;
  margin-bottom: 2%;
  width: 14%;
}
.add-friends-name-btn-container {
  width: 95%;
  margin: 0 auto;
  padding-bottom: 2%;
}
.add-friends-icon {
  margin-left: 1%;
  margin-right: 3%;
}
.add-friends-items {
 padding: 0 8% 0 8%;
 height: 95%;
}
.add-friends-title {
  text-align: left;
  padding: 3% 4% 2% 4%;
}
.name-input {
  border-radius: 15px;
  border: none;
  padding: 2%;
  padding-left: 4%;
  margin-bottom: 2%;
}
p {
  margin-bottom: 0;
}
.place-input {
  width: 80vw;
  margin: 0 auto;
  border-radius: 15px;
  border: none;
  padding: 2%;
  padding-left: 4%;
  margin-bottom: 2%;

}
.search-address {
  color: #ada4a5;
  font-size: 0.7rem;
}
.search-divide {
  margin: 0 auto;
}
.search-item {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin: 4% 0;
}
.search-place {
  font-weight: bold;
}
.search-result {
  position: absolute;
  height: 45vh;
  overflow-y: scroll;
  z-index: 100;
  margin: 0 auto;
  background-color: white;
  border-radius: 15px;
  width: 80vw;
  margin: 0 2%;
  border: solid 1px #e9edfe;
  z-index: 1000;
}
</style>