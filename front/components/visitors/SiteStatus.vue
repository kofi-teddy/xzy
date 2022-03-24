<template>
  <div>
    <div class="inner">
        <h2>{{ site.title }}</h2>
        <IndicatorIcon 
          class="rightfloat" 
          :status="status" 
          :text="false" 
          />
      <div 
          v-for="j in site.uptime_set" 
          :key="j.id"
          class="uptime"
          >
          <div :class="'small-square-indicator ' + j.status"></div>
      </div>
    </div>
  </div>
</template>

<script>
import IndicatorIcon from '@/components/visitors/general/IndicatorIcon'

export default {
  name: 'SiteStatus',
  components: { IndicatorIcon },
  props: {
    site: {
      type: Object,
      default: () => { return {} }
    }
  },
  computed: {
    closedIncidents () {
      return this.$store.state.incidents.filter(a => a.solved)
    }
  }
}
</script>

<style scoped>
.rightfloat {
  float: right;
  margin-top: 13px;
}
h2 {
  display: inline-block;
  width: 50%;
}
.small-square-indicator {
  width: 100%;
  height: 5px;
  display: inline-block;
}
.uptime {
  display: inline-block;
  width: 3.33%;
}
</style>