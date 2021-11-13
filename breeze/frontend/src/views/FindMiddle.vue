<template>
  <div>
    <MiddleMap class="find-middle" />
    <MiddleList class="middle-lists" />
    <FindPlaceBtn class="find-place-btn" />
  </div>
</template>

<script>
import FindPlaceBtn from "@/components/findmiddle/FindPlaceBtn.vue"
import MiddleList from "@/components/findmiddle/MiddleList.vue"
import MiddleMap from "@/components/findmiddle/MiddleMap.vue"
import store from "@/store"

export default {
  name: "FindMiddle",
  components: {
    FindPlaceBtn,
    MiddleList,
    MiddleMap,
  },
  beforeRouteEnter(to, from, next) {
    if (from.name == "EnterInfo" || from.name == "OneClick") {
      store.dispatch("setIsMapRendered", false)
      store.dispatch("setMiddle", 0)
      store.dispatch("setMiddleLists", [])
      store.dispatch("setMode1", 0)
      next()
    } else {
      next()
    }
  },
}
</script>

<style scoped>
.find-middle {
  height: 57%;
}
.find-place-btn {
  height: 14%;
}
.middle-lists {
  height: 29%;
}
</style>