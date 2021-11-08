<template>
  <v-date-picker mode="dateTime" v-model="date" class="choose-date" :min-date="startDate" :model-config="modelConfig">
    <template v-slot="{ inputValue, togglePopover }">
      <div
        class="choose-date-box"
        @click="togglePopover()">
        <button class="choose-date-btn">
          <i class="far fa-calendar-alt"></i>
        </button>
        <input
          placeholder="약속 날짜를 선택해주세요."
          :value="inputValue"
          class="choose-date-input text-gray-700 w-full py-1 px-2 appearance-none rounded-r focus:outline-none focus:border-blue-500"
          readonly
        />
      </div>
    </template>
  </v-date-picker>
</template>

<script>
import { mapActions } from 'vuex'
import dayjs from 'dayjs'

export default {
  name: 'ChooseDate',
  data() {
    return {
      date: '',
      timezone: 'Asia/Seoul',
      startDate: dayjs().toISOString(),
      modelConfig: {
        type: 'string',
        mask: 'YYYY-MM-DD HH:mm'
      }
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
  },
}
</script>

<style scoped>
* {
    color: #ADA4A5;
  }
.choose-date {
  /* margin: 4%; */
  /* height: 30%; */
}
.choose-date-box {
  /* width: 100%; */
  /* height: 100%; */
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
.choose-date-input {
  background-color: #F7F8F8;
  border: none;
  text-align: left;
}
</style>