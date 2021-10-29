<template>
  <div class="choose-date">
    <v-date-picker mode="dateTime" class="inline-block h-full" v-model="date">
      <template v-slot="{ inputValue, togglePopover }">
        <div
          class="choose-date-box"
          @click="togglePopover()">
          <button class="choose-date-btn">
            <i class="far fa-calendar-alt"></i>
          </button>
          <input
            placeholder="약속 날짜를 선택해주세요"
            :value="inputValue"
            style="background-color: #F7F8F8; border: none; text-align: left;"
            class="text-gray-700 w-full py-1 px-2 appearance-none rounded-r focus:outline-none focus:border-blue-500"
            readonly
          />
        </div>
      </template>
    </v-date-picker>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ChooseDate',
  data() {
    return {
      date: '',
      timezone: 'Asia/Seoul'
    }
  },
  methods: {
    ...mapActions([
      'setDate'
    ])
  },
  computed: {
    chooseDate () {
      return this.date
    },
  },
  watch: {
    chooseDate (val) {
      this.setDate(val)
    }
  }
}
</script>

<style scoped>
* {
    color: #ADA4A5;
  }
.choose-date {
  margin: 4%;
}
.choose-date-box {
  width: 90%;
  margin: 0 auto;
  border-radius: 15px;
  background-color: #F7F8F8;
  padding: 1%;
  padding-left: 3%;
  text-align: left;
}
.choose-date-btn {
  border: none;
  background-color: #F7F8F8;
}
</style>