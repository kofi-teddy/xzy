<template>
  <div>
    <div class="cards">
      <div
          v-for="site in sites"
          :key="site.id"
          class="card status"
        >
          <site-status :site="site" />
      </div>
      <div
        v-if="openIncidents.length > 0" 
        class="card incidents" 
      >
        <div
          v-for="i in openIncidents"
          :key="i.id"
          class="incident_item"
        >
          <nuxt-link :to="{ name: 'incident-id', params: { id: i.id }}">
            <IncidentListItem :incident="i" />
          </nuxt-link>
        </div>
      </div>
      <div class="calendar">
        <HistoryPart />
      </div>
    </div>
  </div>
</template>

<script>
import IncidentListItem from '@/components/visitors/IncidentListItem'
import SiteStatus from '@/components/visitors/SiteStatus'
import HistoryPart from '@/components/visitors/HistoryPart'

export default {
  name: 'IndexPage',
  components: { 
    IncidentListItem, 
    SiteStatus, 
    HistoryPart
    },
  data: () => ({
    openIncidents: [{ id: 1, title: 'Connectivity Issues', update_set: [{ description: 'We have noticed some connectivity issues', date: '2019-10-02 13:00:12', status: 'Investigating' }] }],
    // sites: [{ title: 'API', status: 'up', uptime_set: [{ date: '2022-02-2T13:42:58.085870', id: 1, response_time: 352, status: 'up' }, { date: '2022-03-2T13:43:58.085870', id: 2, response_time: 231, status: 'up' }, { date: '2022-03-2T13:44:58.085870', id: 3, response_time: 123, status: 'down' }, { date: '2022-03-2T13:45:58.085870', id: 4, response_time: 344, status: 'issue' }] }]
    sites: $store.state.sites
  }),
  computed: {
    openIncidents () {
      return this.$store.state.incidents.filter(a => !a.solved)
    }
  }
}
</script>

<style scoped>
.card.status { margin-bottom: 10px; }
.cards {
  max-width: 700px;
  margin: -30px auto 20px;
}
.card {
  border-radius: 10px;
  background-color: white;
  padding: 15px 20px;
  box-shadow: 0 0 3px 1px rgba(163,163,163,0.30);
  -webkit-box-shadow: 0 0 3px 1px rgba(163,163,163,0.30);
  font-family: Montserrat;
  font-weight: 300;
}
.incidents > .incident_item {
  margin-bottom: 30px;
  margin-top: 10px;
}
.incidents > .incident_item:last-child {
  margin-bottom: 10px;
}
.incidents {
  margin-bottom: 30px;
}
.calendar {
  font-family: Montserrat;
  font-weight: 300;
  width: 700px;
  margin: 30px auto 0px;
  font-size: 16px;
}

</style>>
