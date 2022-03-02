<template>
  <div>
    <h2>{{ incident.title }}</h2>
    <p>{{ lastUpdate.description }}</p>
    <div class="sub">
      {{ lastUpdate.date }}
      <span class="right">
        Status: {{ lastUpdate.status }}
      </span>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Incident',
    props: {
        incident: {
        type: Object,
        default: () => { return {} }
        }
    },
    computed: {
        lastUpdate () {
        return this.incident.update_set[0]
        }
    }
}
</script>

<style>
    .sub {
    color: #999999;
    }
    .right {
    float: right;
    }
    h2 {
    margin-bottom: 10px;
    }
</style>