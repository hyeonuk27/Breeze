<template>
  <div >
    <ChooseDate class="choose-date" />
    <AddFriends class="add-friends" />
    <ParticipantList class="participant-list" />
    <FindMiddleBtn class="find-middle-btn" />
  </div>
</template>

<script>
import AddFriends from "@/components/enterinfo/AddFriends.vue"
import ChooseDate from "@/components/enterinfo/ChooseDate.vue"
import FindMiddleBtn from "@/components/enterinfo/FindMiddleBtn.vue"
import ParticipantList from "@/components/enterinfo/ParticipantList.vue"
import store from "@/store"

export default {
  name: "EnterInfo",
  components: {
    AddFriends,
    ChooseDate,
    FindMiddleBtn,
    ParticipantList,
  },
  beforeRouteEnter(to, from, next) {
    var isGroup
    if (store.getters.getGroupId == null) {
      isGroup = false
    } else {
      isGroup = true
    }
    if (from.name == "OneClick" || from.name == "MakeAppointment" || isGroup) {
      store.dispatch("setDate", "")
      store.dispatch("setGroupId", null)
      store.dispatch("setGroupName", "")
      store.dispatch("setIsFirst", false)
      store.dispatch("setMiddleLat", 0)
      store.dispatch("setMiddleLong", 0)
      store.dispatch("setMiddleName", "")
      store.dispatch("setParticipants", [])
      store.dispatch("setPartMidTime", [])
      next()
    } else {
      next()
    }
  },
}
</script>

<style scoped>
.add-friends {
  height: 30%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.find-middle-btn {
  height: 14%;
}
.choose-date {
  height: 11%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
.participant-list {
  height: 45%;
}
</style>