<template>
  <div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      notifikasi: {
        active: false,
        message: null,
      }
    }
  },
  name: "LoginPage",
  mounted() {
    this.login()
  },
  methods: {
    login() {
      if (!this.$router.currentRoute.query.ticket) {
        window.location.href = 'https://sso.umkt.ac.id/cas/login?service=' + window.location.origin + this.$router.currentRoute.path
      } else {
        console.log(this.$router.currentRoute.query.ticket)
        axios.post(process.env.VUE_APP_BASE_URL + '/api/auth/', {
          service: window.location.origin + this.$route.path,
          ticket: this.$router.currentRoute.query.ticket
        })
        .then(resp => {
          this.$store.commit('auth', resp.data)
          this.$router.push({ path: '/' })
        })
        .catch(e => console.log(e))
        // try {
        //   this.$auth.loginWith('local', {data: this.model})
        //       .then(() => this.$toast.success('Logged In!')).then(this.$router.push('/'))
        // } catch (e) {
        //   console.log(e)
        //   this.$router.push('/')
        // }


      }
    }
    // login() {
    //   console.log(process.env.VUE_APP_BASE_URL + "/api/auth/")
    //   axios.post(process.env.VUE_APP_BASE_URL + "/api/auth/", {
    //     nim: this.nim,
    //     password: this.password
    //   })
    //       .then(resp => {
    //         this.$store.commit('auth', resp.data)
    //       })
    //       .catch(e => {
    //         console.log(e)
    //       })
    //       .finally(() => {
    //         if (this.$store.state.auth.token !== null) {
    //           this.notifikasi.active = false
    //           this.notifikasi.massage = null
    //           this.$router.push({name: 'login', query: {redirect: '/dashboard'}})
    //         } else {
    //           this.$store.state.notification.active = true
    //           this.notifikasi.massage = 'Akun atau Password Salah'
    //         }
    //       })
    // },
  }
}
</script>

<style scoped>

</style>