<template>
  <div>
    <NotificationBar />
    <TheHeader />
    <transition
      enter-active-class="animated slideInLeft"
      mode="out-in"
      leave-active-class="animated slideOutRight"
      >
      <nuxt />
    </transition>
    <TheFooter />
  </div>
</template>

<script>

import NotificationBar from '@/components/visitors/general/NotificationBar'
import TheHeader from '@/components/visitors/general/TheHeader'
import TheFooter from '@/components/visitors/general/TheFooter'

export default {

  components: { 
    NotificationBar, 
    TheHeader, 
    TheFooter
   }
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
.animated {
  -webkit-animation-duration: 0.2s;
  animation-duration: 0.2s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@keyframes slideInLeft {
  from {
    transform: translate3d(-1%, 0, 0);
    opacity: 0;
    visibility: visible;
  }
  to {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
@keyframes slideOutRight {
  from {
    transform: translate3d(0, 0, 0);
    opacity: 1;
    visibility: visible;
  }
  to {
    opacity: 0;
    transform: translate3d(1%, 0, 0);
  }
}
.slideOutRight {
  animation-name: slideOutRight;
}
.slideInLeft {
  animation-name: slideInLeft;
}
</style>