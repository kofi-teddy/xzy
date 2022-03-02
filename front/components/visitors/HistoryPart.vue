<template>
  <div>
      <div>
    <h2>History</h2>
    <div
        v-for="(i, index) in dates"
        :key="index"
        class="calendar-item"
    >
        <p>{{ i.toDateString() }}</p>
        <div v-if="getIncidents(i).length == 0">
        <font-awesome-icon icon="check-circle" class="green-color" />
        <div class="subtext">
            No incidents
        </div>
        </div>
        <div v-for="j in getIncidents(i)" :key="j.id">
        <font-awesome-icon icon="exclamation-circle" class="orange-color" />
        <div class="subtext issue-name">
            <nuxt-link :to="{ name: 'incident-id', params: { id: j.id }}">
            {{ j.title }}
            </nuxt-link>
            <div class="issue-resolved">
            Resolved on: {{ j.end | dateFormat }}
            </div>
        </div>
        </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'HistoryPart',
    data: (
        dates = [],
        closedIncidents = [
            { 
                id: 1, 
                title: 'Slow response times', 
                end: '2022-03-2 13:00:12', 
                start: '2022-03-1 13:00:12', 
                update_set: [
                    { description: 'We have noticed some connectivity issues', date: '20103-8-1 13:00:12', status: 'Investigating' }
                ] 
            }
        ]
    ),
    mounted(){
        const start = new Date()
        for (let i = 0; i < 6; i++) {
            this.dates.push(new Date(start))
            start.setDate(start.getDate() - 1)
        }
    },

}
</script>

<style>

</style>