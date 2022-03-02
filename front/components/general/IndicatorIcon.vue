<template>
  <div>
      <div :class="'indicator ' + status" />
        <p v-if="showText">
        {{ message }}
        </p>
  </div>
</template>

<script>
export default {
  name: 'IndicatorIcon',
  props: {
    status: {
        type: String,
        default: 'up',
        validator (value) {
        return ['up', 'down', 'issue'].includes(value)
        }
    },
    showText: Boolean
  },
  computed: {
    message () {
      if (this.status === 'up') {
        return 'All is good'
      } else if (this.status === 'down') {
        return 'We are having issues'
      } else if (this.status === 'issue') {
        return 'You might notice some inconvenience'
      } else {
        return 'Invalid'
      }
    }
  }
}
</script>

<style>
.indicator {
  height: 17px;
  width: 17px;
  border-radius: 50%;
  display: inline-block;
}
p {
  display: inline-block;
  position: relative;
  top: -3px;
  margin-left: 5px;
  font-size: 14px;
  color: #464646;
}
</style>