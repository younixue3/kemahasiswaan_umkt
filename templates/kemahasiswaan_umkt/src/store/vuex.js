import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

const state = {
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
        }
    },
    actions: {},
})

export default store