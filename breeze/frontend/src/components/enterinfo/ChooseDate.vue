<template>
  <div class="choose-date-items">
    <v-date-picker
      mode="dateTime"
      v-model="date"
      class="choose-date-picker"
      :min-date="startDate"
      :model-config="modelConfig"
    >
      <template v-slot="{ inputValue, togglePopover }">
        <div class="choose-date-box" @click="togglePopover()">
          <button class="choose-date-btn">
            <i class="far fa-calendar-alt"></i>
          </button>
          <input
            placeholder="약속 날짜를 선택해주세요."
            :value="inputValue"
            class="
              choose-date-input
              text-gray-700
              w-full
              py-1
              px-2
              appearance-none
              rounded-r
            "
            readonly
          />
        </div>
      </template>
    </v-date-picker>
  </div>
</template>

<script>
import { mapActions } from "vuex"
import dayjs from "dayjs"

export default {
  name: "ChooseDate",
  data() {
    return {
      date: "",
      modelConfig: {
        type: "string",
        mask: "YYYY-MM-DD HH:mm",
      },
      startDate: dayjs().toISOString(),
      timezone: "Asia/Seoul",
    }
  },
  methods: {
    ...mapActions(["setDate"]),
  },
  computed: {
    chooseDate() {
      return this.date
    },
  },
  watch: {
    chooseDate(val) {
      this.setDate(val)
    },
  },
}
</script>

<style scoped>
* {
  color: #ada4a5;
}
.choose-date-box {
  width: 100%;
  border-radius: 15px;
  background-color: #f7f8f8;
  padding-left: 3%;
  text-align: left;
  box-shadow: 1.5px 1.5px 2px rgba(197, 197, 197, 0.3);
}
.choose-date-btn {
  display: inline-block;
  border: none;
  background-color: #f7f8f8;
}
.choose-date-input {
  background-color: #f7f8f8;
  border: none;
  text-align: left;
  
}
.choose-date-input:focus {
  outline: none;
}
.choose-date-items {
  padding: 0 8%;
  height: 100%;
}
</style>