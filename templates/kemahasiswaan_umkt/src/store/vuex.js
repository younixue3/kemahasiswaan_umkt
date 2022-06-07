import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
// import axios from "axios";

Vue.use(Vuex)

const state = {
    auth: {
        access_token: null,
        refresh_token: null
    },
    mahasiswa: []
}

const store = new Vuex.Store({
    state,
    getters: {},
    mutations: {
        pushMahasiswa(state, item) {
            state.mahasiswa.push(item)
        },
        deleteMahasiswa(state, item) {
            state.mahasiswa.splice(item, 1);
        },
        auth (state, data) {
            state.auth.access_token = data.access
            state.auth.refresh_token = data.refresh
        },
        authLogout (state) {
            state.auth.status = false
            state.auth.token = null
            state.auth.group = null
            state.auth.superuser = false
            state.auth.name = null
        },
        login (state, ticket, service) {
            state.auth.ticket = ticket
            state.auth.service = service
        }
    },
    actions: {},
    plugins: [createPersistedState()],
})

export default store