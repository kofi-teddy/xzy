<template>
  <div>
    <div class="cards">
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
    </div>
  </div>
</template>

<script>
import IncidentListItem from '@/components/visitors/IncidentListItem'

export default {
  name: 'IndexPage',
  components: { IncidentListItem },
  data: () => ({
    openIncidents: [{ id: 1, title: 'Connectivity Issues', update_set: [{ description: 'We have noticed some connectivity issues', date: '2019-10-02 13:00:12', status: 'Investigating' }] }]
  }),
}
</script>
