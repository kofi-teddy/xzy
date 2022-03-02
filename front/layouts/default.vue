<template>
  <div>
    <nuxt />
    <notification-bar />
  </div>
</template>

<script>

import NotificationBar from '@/components/visitors/general/NotificationBar'

export default {

  components: { NotificationBar }
}
</script>
<style>
body {
  font-family: Montserrat;
}
body, html {
  margin: 0px;
  padding: 0px;
}
h2, h3, h1, h4 {
  margin-top: 5px;
  margin-bottom: 5px;
}
a, a:focus, a:visited, a:hover {
  color: #000;
  text-decoration: none;
}
.issue, .yellow {
  background: #F1C21A;
}
.down, .red {
  background: #CD5C5C;
}
.up, .green {
  background: #2EE779;
}
</style>