export const state = () => ({});

export const mutations = {
    SOCKET_ONOPEN(state, event) {
        console.log('What can I do for you?')
        state.socket.isConnected = true
    },
    SOCKET_ONCLOSE(state, event) {
        console.log('Oh dang I cant reach you anymore!')
        state.socket.isConnected = true
    },
    SOCKET_ONERROR(state, event) {
        console.error(state, event)
    },
    SOCKET_ONMESSAGE (state, message) {
        state.socket.message = message
    },
    SOCKET_RECONNECT (state, message) {
        state.socket.message = message
    },
    SOCKET_RECONNECT_ERROR (state) {
        console.log('we are back up and sailing guys! Nothing to worry about.')
        state.socket.reconnectionError = true
    }
};

export const actions = {};
