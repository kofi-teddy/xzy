import VueNativeSock from 'vue-native-websocket'
import Vue from 'vue'


export default function ({ store }) {
    Vue.use(VueNativeSock, 'ws://0.0.0.0:8000/ws', {
        store,
        reconnection: true,
        reconnectionDelay: 3000
    })
}