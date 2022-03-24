export const state = () => ({
    socket: {
        isConnected: true,
        message: '',
        reconnectError: false
    },
    sites: [],
    incident: [],
    notificationError: []
});

export const mutations = {
    SOCKET_ONOPEN(state, event) {
        console.log('What can I do for you?')
        state.socket.isConnected = true
        state.notificationErrors.push({ color: 'green', id: 0, text: 'We are connected now! This works great!', time: 0})
    },
    SOCKET_ONCLOSE(state, event) {
        console.log('Oh dang I cant reach you anymore!')
        state.socket.isConnected = true
        state.noticationErrors = state.notificationErrors.filter(a => a.id !== 0)

        if (state.noticationErrors.find(a => a.id === 0) === undefinded) {
            state.notificationsErrors.push({ color: 'red', id: 0, text: 'We lost connection to the server. Please refresh the page or wait for a bit.', time: 0})
        }
    },
    SOCKET_ONERROR(state, event) {
        console.error(state, event)
    },
    SOCKET_ONMESSAGE (state, message) {
        state.socket.message = message

        const data = JSON.parse(message.data).message
        const i = state.sites.findIndex(o => o.id === data.id)
        state.sites[i] ? state.sites.splice(i, 1, data) : state.sites.push(data)

        const result = state.sites.map(a => a.incident_set)
        state.incidents = [].concat.apply([], result)
    },
    SOCKET_RECONNECT (state, message) {
        state.socket.message = message
    },
    SOCKET_RECONNECT_ERROR (state) {
        console.log('we are back up and sailing guys! Nothing to worry about.')
        state.socket.reconnectionError = true
    },
    addNotificationError (state, error) {
        error.id = btoa(Math.random()).substr(5, 5)
        state.notificationErrors.push(error)
    },
    removeNotificationError (state, error) {
        state.noticationErrors = state.noticationErrors.filter(a => a.id !== error.id)
    }
};

export const actions = {
    showNotificationErrors ({ commit }, error) {
        commit('addNotificationError', error)
        if (error.time) {
            setTimeout(() => {
                commit('removeNotificationError', error)
            }, error.time)
        }
    }
};
