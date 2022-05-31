import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

const state = {
    auth: {
        status: false,
        token: null,
        group: null,
        superuser: false,
        name: null
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
            if (data.token !== null) {
                state.auth.status = true
                state.auth.token = data.token
                state.auth.group = data.group
                state.auth.superuser = data.superuser
                state.auth.name = data.name
            } else {
                state.auth.status = false
                state.auth.token = null
                state.auth.group = null
                state.auth.superuser = false
                state.auth.name = null
            }
        },
        authLogout (state) {
            state.auth.status = false
            state.auth.token = null
            state.auth.group = null
            state.auth.superuser = false
            state.auth.name = null
        },
    },
    actions: {},
})

export default store