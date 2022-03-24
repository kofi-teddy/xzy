<template>
  <div class="cards">
  <div class="card incidents">
    <h1>{{ incident.title }}</h1>
    <div
      v-for="i in incident.update_set"
      :key="i.id"
      class="incident_item"
    >
      <p>{{ i.description }}</p>
      <div class="half">
        {{ i.date | timeAgo }}
        <span class="right">
          Status: {{ i.status }}
        </span>
      </div>
    </div>
  </div>
  <nuxt-link :to="{ name: 'index' }">
    <div class="back">
      &larr; back
    </div>
  </nuxt-link>
</div>
</template>

<script>
import moment from 'moment'

var timeFormatter = {
  filters: {
    timeAgo(value) {
      return moment.utc(value).fromNow();
    },
  },
};


export default {
    name: 'IncidentDetail',
    mixins: [timeFormatter],
    data: () => ({
        incidents: [{ id: 1, title: 'Connectivity issues', update_set: [{ title: 'Connectivity issues: slow response time API', description: 'We are experiencing connectivity issues on our API. We are investigating this issue and will keep you up to date on this.', date: '2022-03-2 12:30:00', status: 'identified'}, { title: 'We are still investigating this issue.', description: 'We are still working hard on investigating this issue. We appreciate your support and patience.', date: '2022-03-2 12:23:23', status: 'investigating'}] }],
        incident: []
    }),
    computed: {
      incident () {
        return this.$store.state.incidents.find(a => a.id === parseInt(this.$route.params.id))
      }
    },
}
</script>

<style>
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
.half {
  color: #999999;
}
.right {
  float: right;
}
h2 {
  margin-bottom: 10px;
}
</style>