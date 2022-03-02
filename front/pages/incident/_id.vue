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
        {{ i.date }}
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
export default {
    name: 'IncidentDetail',
    data: () => ({
        incidents: [{ id: 1, title: 'Connectivity issues', update_set: [{ title: 'Connectivity issues: slow response time API', description: 'We are experiencing connectivity issues on our API. We are investigating this issue and will keep you up to date on this.', date: '2018-09-12 12:30:00', status: 'identified'}, { title: 'We are still investigating this issue.', description: 'We are still working hard on investigating this issue. We appreciate your support and patience.', date: '2018-08-23 12:23:23', status: 'investigating'}] }],
        incident: []
    }),
    mounted () {
        this.incident = this.incidents.find(a => a.id === parseInt(this.$route.params.id))
    }
}
</script>

<style>

</style>