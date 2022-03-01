<template>
  <div>
        <div
            v-for="i in notificationErrors"
            :key="i.id"
            :class="'full-background ' + i.color"
            >
            {{i.text}}
        </div>
  </div>
</template>

<script>
export default {
  name: 'NotificationBar',
  data: () => ({
    notificationErrors: [{ 'color': 'red', id: 0, text: 'Oh, we are having some issues' }]
  })
}
</script>

<style scoped>
.full-background {
  padding: 10px;
  z-index: 0;
  position: relative;
  text-align: center;
  color: white;
}

</style>