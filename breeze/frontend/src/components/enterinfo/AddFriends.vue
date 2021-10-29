<template>
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
      placeholder="출발지를 입력해주세요.">
    <!-- 출발지 검색 결과 창 -->
    <div v-if="searchWord" class="search-result">
      <div
        v-for="(result, idx) in searchResult"
        :key="idx"
      >
        <div
          class="d-flex align-items-center"
          @click="setLocation(idx)"
          >
          <h3 class="col-2"><i class="fas fa-map-marker-alt"></i></h3>
          <div>
            <p>{{ result.place_name }}</p>
            <p>{{ result.address_name }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row add-friends-name-btn-container">
        <input
          type="text"
          class="col-10 name-input"
          v-model="partName"
          placeholder="이름을 1~6자로 입력해주세요.">
        <button @click="addPart" class="col-2 add-friends-btn">
          <i class="fas fa-plus"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'AddFriends',
  data () {
    return {
      searchWord: '',
      partName: '',
      searchResult: [],
      partLocation: null,
    }
  },
  methods: {
    ...mapActions([
      'addParticipant'
    ]),
    searchPlace () {
      const URL = 'https://dapi.kakao.com/v2/local/search/keyword.json'
      const apiKey = process.env.VUE_APP_KAKAO_API_KEY
      axios.get(URL, {
        headers: {
          'Authorization': apiKey
        },
        params: {
          'query': this.searchWord
        }
      })
      .then((res) => {
        // console.log(res.data.documents)
        this.searchResult = res.data.documents
      })
      .catch((err) => {
        console.log(err)
      })
    },
    setLocation (idx) {
      const target = this.searchResult[idx]
      // console.log(target.place_name)
      this.partLocation = target.place_name
      this.searchWord = target.place_name
      this.searchResult = []
      this.searchWord = ''
    },
    addPart () {
      if (!this.partLocation.trim()) {
        alert('출발지를 입력해주세요')
      } else if (!this.partName.trim()) {
        alert('이름을 입력해주세요')
      } else if (this.partName.trim().length > 6) {
        alert('이름은 1~6자로 입력해주세요')
      } else {
        const data = {
          'baramiType': this.participants.length,
          'name': this.partName,
          'location': this.partLocation
        }
        this.addParticipant(data)
        this.partName = ''
        this.partLocation = ''
        this.searchWord = ''
      }
    }
  },
  computed: {
    ...mapGetters([
      'participants'
    ])
  }
}
</script>

<style>
.add-friends-box {
  background-color: #E9EDFE;
  width: 90%;
  margin: 0 auto;
  border-radius: 15px;
}
.add-friends-title {
  text-align: left;
  padding: 4%;
}
.add-friends-icon {
  margin-left: 1%;
  margin-right: 3%;
}
/* .searchInput {
  width: 65%;
  margin: 0 auto;
} */
.place-input {
  width: 95%;
  margin: 0 auto;
  border-radius: 15px;
  border: none;
  padding: 3%;
  padding-left: 5%;
  margin-bottom: 2%;
}
.name-input {
  border-radius: 15px;
  border: none;
  padding: 3%;
  padding-left: 5%;
  margin-bottom: 2%;

}
.add-friends-name-btn-container {
  width: 95%;
  margin: 0 auto;
}
.add-friends-btn {
  background: linear-gradient(to left, #92A3FD, #9DCEFF);
  border: none;
  border-radius: 20px;
  padding: 3% 2%;
  color: white;
  font-size: 10pt;
  margin-bottom: 2%;
}
.search-result {
  position: absolute;
  height: 40%;
  overflow-y: scroll;
  /* z-index: 100; */
  width: 90%;
  margin: 0 auto;
  background-color: white;
  border-radius: 15px;
}
</style>