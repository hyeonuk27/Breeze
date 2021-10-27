<template>
  <div>
    <v-date-picker mode="dateTime" class="inline-block h-full" v-model="date">
      <template v-slot="{ inputValue, togglePopover }">
        <div
          class="flex items-center"
          @click="togglePopover()">
          <button>
            <i class="far fa-calendar-alt"></i>
          </button>
          <input
            :value="inputValue"
            class="bg-white text-gray-700 w-full py-1 px-2 appearance-none border rounded-r focus:outline-none focus:border-blue-500"
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
      date: new Date(),
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

<style>
.vc-popover-content-wrapper {
  text-align: center;
}
</style>