<template>
  <div class="header-items">
    <div v-if="$route.name == 'Home'">내 약속</div>
    <div v-if="$route.name == 'EnterInfo'">약속 만들기</div>
    <MiddlePlaceMode v-if="$route.name == 'FindMiddle'"/>
    <PlaceMode v-if="$route.name == 'FindPlace'"/>
    <div v-if="$route.name == 'MakeAppointment'">약속 쪽지</div>
    <div v-if="$route.name == 'OneClick'">원클릭 약속 만들기</div>
  </div>
</template>

<script>
import MiddlePlaceMode from '@/components/mode/MiddlePlaceMode'
import PlaceMode from '@/components/mode/PlaceMode'

export default {
  name: 'Header',
  components: {
    MiddlePlaceMode,
    PlaceMode,
  },
  data() {
    return {
    }
  },
  methods: {

  }
}
</script>
<style scoped>
  .header-items {
    width: 100%;
    height: 100%;
    color: white;
    font-weight: 600;
    letter-spacing: 2px;
    display: table;
  }
  .header-items div {
    display: table-cell;
    vertical-align: middle;
  }
</style>